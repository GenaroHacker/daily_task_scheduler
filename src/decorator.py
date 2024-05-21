import os
import sqlite3
import traceback
from datetime import datetime


class FunctionTracker:
    DB_PATH = os.path.join("assets", "data", "smark.db")

    def __init__(self, func):
        self.func = func
        self.start_time = None
        self.error_log_file = os.path.join("error.log")
        self.initialize_database()

    def initialize_database(self):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    function_name TEXT,
                    action_type TEXT,
                    timestamp DATETIME
                )
            """
            )
            conn.commit()

    def __call__(self, *args, **kwargs):
        self.prepare_execution()
        if self.decide_execution():
            return self.execute_function(*args, **kwargs)
        else:
            self.skip_function()

    def prepare_execution(self):
        os.system("clear")
        print(f"Preparing to execute function: \033[33m{self.func.__name__}\033[0m")

    def decide_execution(self):
        decision = input("Execute? Press Enter to execute or type 'skip' to skip:\n")
        return decision.lower() != "skip"

    def execute_function(self, *args, **kwargs):
        self.start_time = datetime.now()
        try:
            result = self.func(*args, **kwargs)
        except Exception as e:
            with open(self.error_log_file, "w") as f:
                f.write(traceback.format_exc())
            return
        self.complete_task()
        return result

    def complete_task(self):
        end_time = datetime.now()
        self.log_events(self.func.__name__, self.start_time, end_time)
        self.display_execution_time(end_time)
        input("\033[92mTask completed! Press Enter to continue...\033[0m")

    def skip_function(self):
        self.log_event(self.func.__name__, "skipped")
        print("Skipping task.")

    def log_events(self, function_name, start_time, end_time):
        events = [
            (function_name, "start", start_time),
            (function_name, "end", end_time),
        ]
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.executemany(
                """
                INSERT INTO events (function_name, action_type, timestamp)
                VALUES (?, ?, ?)
            """,
                [
                    (name, action, timestamp.isoformat())
                    for name, action, timestamp in events
                ],
            )
            conn.commit()

    def log_event(self, function_name, action_type):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO events (function_name, action_type, timestamp)
                VALUES (?, ?, ?)
            """,
                (function_name, action_type, datetime.now().isoformat()),
            )
            conn.commit()

    def display_execution_time(self, end_time):
        duration = (end_time - self.start_time).total_seconds()
        print(f"Time taken for this execution: {duration:.2f} seconds")
        self.compare_with_average(self.func.__name__, duration)

    def compare_with_average(self, function_name, current_duration):
        average_duration = self.calculate_average_duration(function_name)
        if average_duration > 0:  # Check to prevent division by zero
            deviation = ((current_duration - average_duration) / average_duration) * 100
            color = "\033[91m" if deviation > 0 else "\033[92m"
            print(
                f"{color}This time it took {abs(deviation):.2f}% {'more' if deviation > 0 else 'less'} than the average.\033[0m"
            )
        else:
            print("No prior executions to compare against.")

    def calculate_average_duration(self, function_name):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            # Retrieve all start and end timestamps for the specified function, sorted to ensure pairing
            cursor.execute(
                """
                SELECT action_type, timestamp FROM events
                WHERE function_name = ? AND (action_type = 'start' OR action_type = 'end')
                ORDER BY timestamp
            """,
                (function_name,),
            )
            records = cursor.fetchall()

        # Separate and pair the start and end timestamps
        paired_timestamps = []
        start_time = None

        for action, timestamp in records:
            timestamp = datetime.fromisoformat(timestamp)
            if action == "start":
                start_time = timestamp
            elif action == "end" and start_time is not None:
                paired_timestamps.append((start_time, timestamp))
                start_time = None  # Reset start time after pairing

        # Calculate durations from paired timestamps
        durations = [
            ((end - start).total_seconds()) for start, end in paired_timestamps
        ]

        # Return the average of durations, or zero if there are no complete pairs
        return sum(durations) / len(durations) if durations else 0


def track_function(func):
    return FunctionTracker(func)
