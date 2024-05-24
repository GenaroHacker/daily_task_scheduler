import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from datetime import datetime, timedelta


def plot_task_time_distribution(db_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch all records from the table 'events'
    cursor.execute("SELECT * FROM events")
    records = cursor.fetchall()

    # Get column names
    column_names = [description[0] for description in cursor.description]

    # Close the database connection
    conn.close()

    # Create a DataFrame
    records_df = pd.DataFrame(records, columns=column_names)

    # Filter out the 'skipped' records
    filtered_df = records_df[records_df["action_type"] != "skipped"]

    # Convert the timestamp to datetime
    filtered_df["timestamp"] = pd.to_datetime(filtered_df["timestamp"])

    # Calculate time intervals for each task
    task_times = []
    for function_name, group in filtered_df.groupby("function_name"):
        starts = group[group["action_type"] == "start"]["timestamp"]
        ends = group[group["action_type"] == "end"]["timestamp"]
        for start, end in zip(starts, ends):
            task_times.append(
                {
                    "function_name": function_name,
                    "duration": (end - start).total_seconds(),
                    "timestamp": start,
                }
            )

    task_times_df = pd.DataFrame(task_times)

    # Current date and time for reference
    now = datetime.now()

    # Define time intervals
    one_day_ago = now - timedelta(days=1)
    one_week_ago = now - timedelta(weeks=1)
    one_month_ago = now - timedelta(days=30)

    # Filter data for each time interval
    daily_df = task_times_df[task_times_df["timestamp"] >= one_day_ago]
    weekly_df = task_times_df[task_times_df["timestamp"] >= one_week_ago]
    monthly_df = task_times_df[task_times_df["timestamp"] >= one_month_ago]

    # Calculate total time per task for each interval
    daily_total_time = daily_df.groupby("function_name")["duration"].sum()
    weekly_total_time = weekly_df.groupby("function_name")["duration"].sum()
    monthly_total_time = monthly_df.groupby("function_name")["duration"].sum()

    def consolidate_small_tasks(data, threshold=0.02):
        total_time = data.sum()
        consolidated_data = data.copy()
        others = consolidated_data[consolidated_data / total_time < threshold].sum()
        consolidated_data = consolidated_data[
            consolidated_data / total_time >= threshold
        ]
        if others > 0:
            consolidated_data["others"] = others
        return consolidated_data.sort_values(ascending=False)

    daily_total_time = consolidate_small_tasks(daily_total_time)
    weekly_total_time = consolidate_small_tasks(weekly_total_time)
    monthly_total_time = consolidate_small_tasks(monthly_total_time)

    def order_legend_labels(data):
        data_sorted = data.sort_values(ascending=False)
        if "others" in data_sorted.index:
            others = data_sorted.pop("others")
            data_sorted["others"] = others
        return data_sorted

    daily_total_time = order_legend_labels(daily_total_time)
    weekly_total_time = order_legend_labels(weekly_total_time)
    monthly_total_time = order_legend_labels(monthly_total_time)

    # Hardcoded colors
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

    # Define hatch patterns
    hatch_patterns = [
        '/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*'
    ]

    # Assign colors and hatch patterns to labels
    all_labels = list(
        set(daily_total_time.index)
        | set(weekly_total_time.index)
        | set(monthly_total_time.index)
    )
    colors = {
        label: color_list[i % len(color_list)] for i, label in enumerate(all_labels)
    }
    hatches = {
        label: hatch_patterns[i % len(hatch_patterns)] for i, label in enumerate(all_labels)
    }

    # Plotting
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))

    def plot_pie(ax, data, title):
        colors_for_pie = [colors[label] for label in data.index]
        hatches_for_pie = [hatches[label] for label in data.index]
        wedges, texts, autotexts = ax.pie(
            data, startangle=140, autopct="%1.1f%%", colors=colors_for_pie
        )
        for i, patch in enumerate(wedges):
            patch.set_hatch(hatches_for_pie[i])
        ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.set_title(title)
        ax.legend(
            wedges,
            data.index,
            title="Tasks",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1),
        )

    plot_pie(axs[0], monthly_total_time, "Last 30 Days Time Distribution")
    plot_pie(axs[1], weekly_total_time, "Last 7 Days Time Distribution")
    plot_pie(axs[2], daily_total_time, "Today's Time Distribution")

    plt.tight_layout()
    plt.show()
