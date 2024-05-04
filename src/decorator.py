import os
import sqlite3
import time
from datetime import datetime

class FunctionTracker:
    DB_PATH = os.path.join('assets', 'data', 'history.db')

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        self.prepare_db()
        self.print_function_name()
        if self.user_decides_to_skip():
            return
        start_time = datetime.now()
        self.log_action("started", start_time)
        try:
            result = self.func(*args, **kwargs)
        except Exception as e:
            self.handle_exception(e)
            return
        finally:
            self.prompt_continue("\033[92mTask completed! Press Enter to continue...\033[0m")

        end_time = datetime.now()
        self.log_action("completed", end_time)
        duration = (end_time - start_time).total_seconds()
        self.report_time_taken(duration)
        os.system('clear')
        return result

    def prepare_db(self):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            # Use a single query to check for and optionally delete the last "started" entry
            cursor.execute("""
            DELETE FROM events WHERE id = (SELECT id FROM events WHERE action = 'started' ORDER BY id DESC LIMIT 1)
            """)
            conn.commit()

    def print_function_name(self):
        print(f"Executing function: {self.func.__name__}")

    def user_decides_to_skip(self):
        user_input = input("Press Enter to start or write 'skip' to skip: ")
        return user_input.lower() == 'skip'

    def log_action(self, action, timestamp):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO events (function, action, timestamp) VALUES (?, ?, ?)",
                           (self.func.__name__, action, timestamp.isoformat()))
            conn.commit()

    def handle_exception(self, exception):
        print(f"An error occurred: {exception}")
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            DELETE FROM events WHERE id = (SELECT id FROM events WHERE function = ? AND action = 'started' ORDER BY id DESC LIMIT 1)
            """, (self.func.__name__,))
            conn.commit()
        input("An error has occurred. Press Enter to continue...")

    def prompt_continue(self, message):
        input(message)

    def report_time_taken(self, duration):
        print(f"Time taken for this execution: {duration:.2f} seconds")
        self.compare_with_average(duration)

    def compare_with_average(self, current_duration):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT timestamp FROM events WHERE function = ? AND action = 'completed'
            ORDER BY id
            """, (self.func.__name__,))
            timestamps = [datetime.fromisoformat(record[0]) for record in cursor.fetchall()]

            if len(timestamps) >= 2:  # Need at least two completed cycles
                durations = [(timestamps[i] - timestamps[i-1]).total_seconds() for i in range(1, len(timestamps))]
                average_duration = sum(durations) / len(durations)
                deviation = ((current_duration - average_duration) / average_duration) * 100
                color = "\033[91m" if deviation > 0 else "\033[92m"
                print(f"{color}This time it took {abs(deviation):.2f}% {'more' if deviation > 0 else 'less'} than the average.\033[0m")
                print("\n\n\n\n\n\n\n\n\n")

def track_function(func):
    return FunctionTracker(func)

