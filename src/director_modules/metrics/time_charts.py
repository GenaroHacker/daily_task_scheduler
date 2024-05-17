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
    filtered_df = records_df[records_df['action_type'] != 'skipped']

    # Convert the timestamp to datetime
    filtered_df['timestamp'] = pd.to_datetime(filtered_df['timestamp'])

    # Calculate time intervals for each task
    task_times = []
    for function_name, group in filtered_df.groupby('function_name'):
        starts = group[group['action_type'] == 'start']['timestamp']
        ends = group[group['action_type'] == 'end']['timestamp']
        for start, end in zip(starts, ends):
            task_times.append({
                'function_name': function_name,
                'duration': (end - start).total_seconds(),
                'timestamp': start
            })

    task_times_df = pd.DataFrame(task_times)

    # Current date and time for reference
    now = datetime.now()

    # Define time intervals
    one_day_ago = now - timedelta(days=1)
    one_week_ago = now - timedelta(weeks=1)
    one_month_ago = now - timedelta(days=30)

    # Filter data for each time interval
    daily_df = task_times_df[task_times_df['timestamp'] >= one_day_ago]
    weekly_df = task_times_df[task_times_df['timestamp'] >= one_week_ago]
    monthly_df = task_times_df[task_times_df['timestamp'] >= one_month_ago]

    # Calculate total time per task for each interval
    daily_total_time = daily_df.groupby('function_name')['duration'].sum()
    weekly_total_time = weekly_df.groupby('function_name')['duration'].sum()
    monthly_total_time = monthly_df.groupby('function_name')['duration'].sum()

    # Plotting
    fig, axs = plt.subplots(1, 3, figsize=(12, 6))

    def plot_pie(ax, data, title):
        ax.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.set_title(title)

    plot_pie(axs[0], daily_total_time, 'Daily Time Distribution')
    plot_pie(axs[1], weekly_total_time, 'Weekly Time Distribution')
    plot_pie(axs[2], monthly_total_time, 'Monthly Time Distribution')

    plt.tight_layout()
    plt.show()

