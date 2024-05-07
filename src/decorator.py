import os
import sqlite3
from datetime import datetime
import traceback

class FunctionTracker:
    DB_PATH = os.path.join('assets', 'data', 'history.db')

    def __init__(self, func):
        self.func = func
        self.start_time = None
        self.initialize_database()

    def initialize_database(self):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    function_name TEXT,
                    action_type TEXT,
                    timestamp DATETIME
                )
            ''')
            conn.commit()

    def __call__(self, *args, **kwargs):
        os.system('clear')
        print(f"Executing function: {self.func.__name__}\n\n")
        decision = input("Execute? Press Enter to execute or type 'skip' to skip:\n")
        if decision.lower() == 'skip':
            self.log_event(self.func.__name__, 'skipped')
            print("Skipping task.")
            return

        self.start_time = datetime.now()
        try:
            result = self.func(*args, **kwargs)
        except Exception:
            traceback.print_exc()
            return
        finally:
            self.end_task()

        return result

    def end_task(self):
        end_time = datetime.now()
        if self.start_time:
            self.log_event(self.func.__name__, 'end', end_time)
            duration = (end_time - self.start_time).total_seconds()
            self.compare_with_average(self.func.__name__, duration)
            print(f"Time taken for this execution: {duration:.2f} seconds")

        input("\033[92mTask completed! Press Enter to continue...\033[0m")

    def log_event(self, function_name, action_type, timestamp=None):
        if not timestamp:
            timestamp = datetime.now()
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO events (function_name, action_type, timestamp)
                VALUES (?, ?, ?)
            ''', (function_name, action_type, timestamp.isoformat()))
            conn.commit()

    def compare_with_average(self, function_name, current_duration):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT julianday(timestamp) FROM events
                WHERE function_name = ? AND action_type = 'end'
            ''', (function_name,))
            timestamps = cursor.fetchall()
            if timestamps and len(timestamps) > 1:
                average_duration = self.calculate_average_duration(timestamps)
                deviation = ((current_duration - average_duration) / average_duration) * 100
                color = "\033[91m" if deviation > 0 else "\033[92m"
                print(f"{color}This time it took {abs(deviation):.2f}% {'more' if deviation > 0 else 'less'} than the average.\033[0m")

    def calculate_average_duration(self, timestamps):
        durations = [t1 - t0 for t0, t1 in zip(timestamps[:-1], timestamps[1:])]
        average_duration = sum(durations) / len(durations)
        return average_duration

def track_function(func):
    return FunctionTracker(func)
