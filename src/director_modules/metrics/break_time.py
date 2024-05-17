import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from datetime import datetime, timedelta

def plot_work_vs_break_time_distribution(db_path):
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

    # Calculate work time and break time for each day
    daily_times = []
    for date, group in filtered_df.groupby(filtered_df['timestamp'].dt.date):
        starts = group[group['action_type'] == 'start']['timestamp']
        ends = group[group['action_type'] == 'end']['timestamp']

        # Ensure the data is in chronological order
        starts = starts.sort_values()
        ends = ends.sort_values()

        if not starts.empty and not ends.empty:
            first_start = starts.iloc[0]
            last_end = ends.iloc[-1]
            total_work_period = (last_end - first_start).total_seconds()

            # Calculate break time
            break_time = 0
            for start, end in zip(starts[1:], ends[:-1]):
                break_time += (start - end).total_seconds()

            actual_work_time = total_work_period - break_time

            daily_times.append({
                'date': date,
                'work_time': actual_work_time,
                'break_time': break_time
            })

    daily_times_df = pd.DataFrame(daily_times)

    # Current date and time for reference
    now = datetime.now()

    # Define time intervals
    one_day_ago = now - timedelta(days=1)
    one_week_ago = now - timedelta(weeks=1)
    one_month_ago = now - timedelta(days=30)

    # Filter data for each time interval
    daily_df = daily_times_df[daily_times_df['date'] >= one_day_ago.date()]
    weekly_df = daily_times_df[daily_times_df['date'] >= one_week_ago.date()]
    monthly_df = daily_times_df[daily_times_df['date'] >= one_month_ago.date()]

    # Calculate total work and break time for each interval
    daily_work_time = daily_df['work_time'].sum()
    daily_break_time = daily_df['break_time'].sum()
    weekly_work_time = weekly_df['work_time'].sum()
    weekly_break_time = weekly_df['break_time'].sum()
    monthly_work_time = monthly_df['work_time'].sum()
    monthly_break_time = monthly_df['break_time'].sum()

    # Plotting
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))

    def plot_pie(ax, work_time, break_time, title):
        data = [work_time, break_time]
        labels = ['Work Time', 'Break Time']
        colors = ['red', 'grey']
        ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.set_title(title)

    plot_pie(axs[0], monthly_work_time, monthly_break_time, 'Monthly Time Distribution')
    plot_pie(axs[1], weekly_work_time, weekly_break_time, 'Weekly Time Distribution')
    plot_pie(axs[2], daily_work_time, daily_break_time, 'Daily Time Distribution')

    plt.tight_layout()
    plt.show()

