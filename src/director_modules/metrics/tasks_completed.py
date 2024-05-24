import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import matplotlib.dates as mdates

def plot_event_schedule(db_path, days_range=None):
    # Connect to the database
    conn = sqlite3.connect(db_path)

    # Load data from the events table
    query = "SELECT * FROM events"
    df = pd.read_sql_query(query, conn)
    conn.close()

    # Convert timestamp to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Filter out 'skipped' action_type
    df = df[df["action_type"] != "skipped"]

    # Filter data by the specified days range
    if days_range is not None:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days_range)
        df = df[(df["timestamp"] >= start_date) & (df["timestamp"] <= end_date)]

    # Extract unique dates
    df["date"] = df["timestamp"].dt.date
    unique_dates = df["date"].unique()

    # Create a dictionary to store tasks by date and a dictionary for task durations
    schedule = {date: [] for date in unique_dates}
    task_durations = {}
    for date in unique_dates:
        day_events = df[df["date"] == date]
        for function_name in day_events["function_name"].unique():
            task_events = day_events[day_events["function_name"] == function_name]
            start_times = task_events[task_events["action_type"] == "start"]["timestamp"]
            end_times = task_events[task_events["action_type"] == "end"]["timestamp"]
            for start, end in zip(start_times, end_times):
                schedule[date].append((start, end, function_name))
                duration = (end - start).total_seconds() / 3600
                task_durations[function_name] = (
                    task_durations.get(function_name, 0) + duration
                )

    # Sort tasks by duration
    sorted_tasks = sorted(task_durations.items(), key=lambda x: x[1], reverse=True)[:30]

    # High-contrast hardcoded colors
    color_list = [
        "#ff0000",
        "#00ffff",
        "#7fff00",
        "#7f00ff",
        "#ff00aa",
        "#ffaa00",
        "#00ff55",
        "#0054ff",
        "#2aff00",
        "#2a00ff",
    ]

    # Generate random colors for additional tasks if necessary
    total_tasks = len(sorted_tasks)  # Total number of tasks
    if total_tasks > len(color_list):
        additional_colors = plt.cm.rainbow(np.linspace(0, 1, total_tasks - len(color_list)))
        color_list.extend(additional_colors)

    # Define hatch patterns
    hatch_patterns = [
        '/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*'
    ]

    # Extend hatch patterns if necessary
    if total_tasks > len(hatch_patterns):
        hatch_patterns *= (total_tasks // len(hatch_patterns) + 1)
        hatch_patterns = hatch_patterns[:total_tasks]

    # Assign colors and hatch patterns to tasks
    colors = {task: color_list[i] for i, (task, _) in enumerate(sorted_tasks)}
    hatches = {task: hatch_patterns[i] for i, (task, _) in enumerate(sorted_tasks)}

    # Sort dates for plotting
    unique_dates = sorted(unique_dates)

    # Create the plot
    plt.figure(figsize=(12, 6))

    for date in unique_dates:
        tasks = schedule[date]
        for start, end, function_name in tasks:
            if function_name in colors:
                start_hour = start.hour + start.minute / 60
                end_hour = end.hour + end.minute / 60
                plt.bar(
                    date,
                    end_hour - start_hour,
                    bottom=start_hour,
                    color=colors[function_name],
                    edgecolor="grey",
                    hatch=hatches[function_name],
                    label=function_name,
                )

    # Add vertical lines for Mondays
    for date in unique_dates:
        if date.weekday() == 0:  # Monday
            plt.axvline(date, color="grey", linestyle="--", linewidth=1)

    # Formatting x-axis
    plt.xticks(unique_dates)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.xticks(rotation=90)  # Rotate date labels perpendicular

    # Set y-axis range to 24 hours
    plt.ylim(0, 24)
    plt.yticks(np.arange(0, 25, 1))  # Include 24-hour numbers

    # Add labels and title
    plt.xlabel("Days")
    plt.ylabel("Hours")
    plt.title("Event Schedule with Gaps")

    # Add gridlines
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)

    # Add legend on the side
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(
        by_label.values(),
        by_label.keys(),
        loc="center left",
        bbox_to_anchor=(1, 0.5),
        ncol=1,
    )

    # Show plot
    plt.tight_layout(rect=[0, 0, 0.85, 1])
    plt.show()
