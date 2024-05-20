def plot_work_vs_break_time_distribution(db_path):
    import sqlite3
    import pandas as pd
    import datetime as dt
    import matplotlib.pyplot as plt

    def fetch_events(db_path):
        conn = sqlite3.connect(db_path)
        query = "SELECT * FROM events"
        events_df = pd.read_sql_query(query, conn)
        conn.close()
        events_df['timestamp'] = pd.to_datetime(events_df['timestamp'])
        return events_df

    def calculate_daily_times(df, date):
        day_events = df[df['timestamp'].dt.date == date].sort_values(by='timestamp')
        work_time = dt.timedelta()
        break_time = dt.timedelta()
        
        last_end = None
        start_time = None
        first_start = None
        last_end_time = None
        
        for _, row in day_events.iterrows():
            if row['action_type'] == 'start':
                start_time = row['timestamp']
                if first_start is None:
                    first_start = start_time
            elif row['action_type'] == 'end' and start_time is not None:
                end_time = row['timestamp']
                work_time += end_time - start_time
                if last_end is not None:
                    break_time += start_time - last_end
                last_end = end_time
                last_end_time = end_time
        
        if first_start is None or last_end_time is None:
            return None, None  # Incomplete data for the day
        
        # Ensure break time is only within the working period
        total_time = last_end_time - first_start
        if break_time > total_time:
            break_time = total_time
        
        return work_time.total_seconds() / 3600, break_time.total_seconds() / 3600

    def calculate_average_times(df, num_days):
        end_date = df['timestamp'].max().date()
        start_date = end_date - dt.timedelta(days=num_days-1)
        
        total_work_time = 0
        total_break_time = 0
        valid_days = 0
        
        for single_date in (start_date + dt.timedelta(n) for n in range(num_days)):
            work_time, break_time = calculate_daily_times(df, single_date)
            if work_time is not None and break_time is not None:
                total_work_time += work_time
                total_break_time += break_time
                valid_days += 1
        
        if valid_days == 0:
            return None, None
        
        average_work_time = total_work_time / valid_days
        average_break_time = total_break_time / valid_days
        
        return average_work_time, average_break_time

    def plot_pie_chart(ax, data, title):
        labels = ['Work Time', 'Break Time']
        colors = ['blue', 'grey']
        ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        ax.set_title(title)

    # Fetch the events
    events_df = fetch_events(db_path)
    today = events_df['timestamp'].max().date()

    # Calculate time distributions
    today_work_time, today_break_time = calculate_daily_times(events_df, today)
    last_7_days_avg_work, last_7_days_avg_break = calculate_average_times(events_df, 7)
    last_30_days_avg_work, last_30_days_avg_break = calculate_average_times(events_df, 30)

    # Data for the pie charts
    last_30_days_data = [last_30_days_avg_work, last_30_days_avg_break]
    last_7_days_data = [last_7_days_avg_work, last_7_days_avg_break]
    today_data = [today_work_time, today_break_time]

    # Create pie charts
    fig, axs = plt.subplots(1, 3, figsize=(12, 6))

    # Plot Last 30 Days Average Time Distribution
    plot_pie_chart(axs[0], last_30_days_data, 'Last 30 Days Average Time Distribution')

    # Plot Last 7 Days Average Time Distribution
    plot_pie_chart(axs[1], last_7_days_data, 'Last 7 Days Average Time Distribution')

    # Plot Today Time Distribution
    plot_pie_chart(axs[2], today_data, 'Today Time Distribution')

    plt.show()

