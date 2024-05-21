# Re-import necessary libraries since the assistant context may not retain previous imports
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from datetime import datetime, timedelta


def plot_daily_skipped_vs_completed_tasks(db_path, days_range=None):
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

    # Convert the timestamp to datetime
    records_df["timestamp"] = pd.to_datetime(records_df["timestamp"])

    # Filter for 'start' and 'end' action types
    filtered_df = records_df[
        records_df["action_type"].isin(["start", "end", "skipped"])
    ]

    # Extract date from timestamp
    filtered_df["date"] = filtered_df["timestamp"].dt.date

    # Calculate daily counts of completed and skipped tasks
    daily_completed = (
        filtered_df[filtered_df["action_type"] == "end"].groupby("date").size()
    )
    daily_skipped = (
        filtered_df[filtered_df["action_type"] == "skipped"].groupby("date").size()
    )

    # Create a DataFrame with both counts
    daily_counts = pd.DataFrame(
        {"Completed": daily_completed, "Skipped": daily_skipped}
    ).fillna(0)

    # If days_range is specified, filter the data
    if days_range is not None:
        start_date = datetime.now().date() - timedelta(days=days_range)
        daily_counts = daily_counts[daily_counts.index >= start_date]

    # Plotting
    fig, ax = plt.subplots(figsize=(12, 6))

    # Plot the bar chart
    daily_counts.plot(kind="bar", ax=ax, color=["blue", "grey"])

    # Set chart title and labels
    ax.set_title("Daily Skipped vs Completed Tasks")
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of Tasks")

    # Display legend
    ax.legend(["Completed", "Skipped"])

    plt.tight_layout()
    plt.show()
