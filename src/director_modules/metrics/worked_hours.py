import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta


def plot_start_and_end_hours(db_path, days_range=None):
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Calculate the date range
    end_date = datetime.now()
    if days_range is None:
        # Query for the earliest date in the database
        query = "SELECT MIN(timestamp) FROM events"
        cursor.execute(query)
        start_date = pd.to_datetime(cursor.fetchone()[0])
    else:
        start_date = end_date - timedelta(days=days_range)

    # Query for 'start' and 'end' events within the date range
    query = """
    SELECT * FROM events 
    WHERE (action_type = 'start' OR action_type = 'end') 
    AND timestamp BETWEEN ? AND ?
    """
    cursor.execute(query, (start_date.isoformat(), end_date.isoformat()))
    records = cursor.fetchall()

    # Convert records to DataFrame
    df = pd.DataFrame(records, columns=["id", "event_type", "action_type", "timestamp"])
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["day"] = df["timestamp"].dt.date
    df["hour"] = df["timestamp"].dt.hour

    # Find the earliest 'start' and latest 'end' event for each day
    daily_start_hours = (
        df[df["action_type"] == "start"].groupby("day")["hour"].min().reset_index()
    )
    daily_end_hours = (
        df[df["action_type"] == "end"].groupby("day")["hour"].max().reset_index()
    )

    # Prepare full range of days for x-axis
    full_days_range = pd.date_range(start=start_date, end=end_date, freq="D")

    # Plotting
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(
        daily_start_hours["day"],
        daily_start_hours["hour"],
        color="blue",
        label="Start Hours",
    )
    ax.scatter(
        daily_end_hours["day"], daily_end_hours["hour"], color="red", label="End Hours"
    )

    # Plot the lines, handling any missing days for start hours
    for i in range(len(daily_start_hours) - 1):
        if (
            daily_start_hours["day"].iloc[i + 1] - daily_start_hours["day"].iloc[i]
        ).days == 1:
            ax.plot(
                [
                    daily_start_hours["day"].iloc[i],
                    daily_start_hours["day"].iloc[i + 1],
                ],
                [
                    daily_start_hours["hour"].iloc[i],
                    daily_start_hours["hour"].iloc[i + 1],
                ],
                "b-",
            )

    # Plot the lines, handling any missing days for end hours
    for i in range(len(daily_end_hours) - 1):
        if (
            daily_end_hours["day"].iloc[i + 1] - daily_end_hours["day"].iloc[i]
        ).days == 1:
            ax.plot(
                [daily_end_hours["day"].iloc[i], daily_end_hours["day"].iloc[i + 1]],
                [daily_end_hours["hour"].iloc[i], daily_end_hours["hour"].iloc[i + 1]],
                "r-",
            )

    # Get all unique dates from the DataFrame
    unique_dates = pd.concat(
        [daily_start_hours["day"], daily_end_hours["day"]]
    ).unique()

    # Highlight Mondays
    for date in unique_dates:
        if date.weekday() == 0:  # Monday
            ax.axvline(date, color="grey", linestyle="--", linewidth=2.0, zorder=-1)

    # Formatting the plot
    ax.set_title(f"Start and End Hours from {start_date.date()} to {end_date.date()}")
    ax.set_xlabel("Day")
    ax.set_ylabel("Hour")

    # Use matplotlib.dates to set major and minor locators and formatters
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

    # Rotate and align the x labels
    fig.autofmt_xdate()

    ax.set_yticks(range(0, 25, 1))
    ax.grid(True)
    ax.legend()

    plt.show()

    # Close the database connection
    conn.close()
