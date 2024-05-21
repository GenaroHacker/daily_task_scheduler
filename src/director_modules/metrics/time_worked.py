import sqlite3
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np


def plot_time_worked(db_path: str, days_range: int = None) -> None:
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)

    # Read the events table into a DataFrame
    events_df = pd.read_sql_query("SELECT * FROM events", conn)

    # Close the database connection
    conn.close()

    # Convert timestamp to datetime
    events_df["timestamp"] = pd.to_datetime(events_df["timestamp"])

    # Filter records with action_type as 'start' and 'end'
    filtered_df = events_df[events_df["action_type"].isin(["start", "end"])]

    # Calculate the date range
    end_date = datetime.now()
    if days_range is None:
        start_date = filtered_df["timestamp"].min()
        days = (end_date - start_date).days
    else:
        start_date = end_date - timedelta(days=days_range)
        days = days_range

    # Calculate total time worked per day
    days_data = {}
    for day in range(days):
        day_start = (end_date - timedelta(days=day)).replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        day_end = day_start + timedelta(days=1)
        day_df = filtered_df[
            (filtered_df["timestamp"] >= day_start)
            & (filtered_df["timestamp"] < day_end)
        ]

        # Group by function_name and pair start and end actions
        total_worked_seconds = 0
        for func in day_df["function_name"].unique():
            func_df = day_df[day_df["function_name"] == func]
            start_times = func_df[func_df["action_type"] == "start"]["timestamp"].values
            end_times = func_df[func_df["action_type"] == "end"]["timestamp"].values

            for start, end in zip(start_times, end_times):
                total_worked_seconds += (end - start) / np.timedelta64(1, "s")

        worked_percentage = (total_worked_seconds / (24 * 3600)) * 100
        days_data[day_start.date()] = worked_percentage

    # Plot the results
    plt.figure(figsize=(12, 6))

    # Add vertical lines for each Monday in the background
    ax = plt.gca()
    for date in days_data.keys():
        if date.weekday() == 0:  # Monday
            ax.axvline(x=date, color="grey", linestyle="--", zorder=0)

    plt.bar(days_data.keys(), days_data.values(), color="blue", zorder=3)

    plt.xlabel("Date")
    plt.ylabel("Percentage of Time Worked")
    plt.title("Percentage of Time Worked per Day")
    plt.ylim(0, 100)  # Set y-axis limits to show full 100%
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
