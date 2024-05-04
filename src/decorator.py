import os
import sqlite3
import time
from datetime import datetime

class FunctionTracker:
    DB_PATH = os.path.join('assets', 'data', 'history.db')

    def __init__(self, func):
        self.func = func
        self.initialize_database()

    def initialize_database(self):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    function_name TEXT,
                    action_type TEXT,
                    timestamp DATETIME,
                    execution_time REAL
                )
            ''')
            conn.commit()

    def __call__(self, *args, **kwargs):
        print(f"Executing function: {self.func.__name__}")
        decision = input("Execute? Press Enter to execute or type 'skip' to skip: ")
        if decision.lower() == 'skip':
            print("Skipping task.")
            return

        start_time = datetime.now()
        self.log_event(self.func.__name__, 'start')
        try:
            result = self.func(*args, **kwargs)
        except Exception as e:
            self.log_event(self.func.__name__, 'failed', (datetime.now() - start_time).total_seconds())
            print(f"An error occurred: {e}")
            return
        finally:
            input("\033[92mTask completed! Press Enter to continue...\033[0m")

        end_time = datetime.now()
        self.log_event(self.func.__name__, 'end', (end_time - start_time).total_seconds())
        duration = (end_time - start_time).total_seconds()
        print(f"Time taken for this execution: {duration:.2f} seconds")
        self.compare_with_average(self.func.__name__, duration)
        time.sleep(3)
        os.system('clear')

    def log_event(self, function_name, action_type, execution_time=None):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO events (function_name, action_type, timestamp, execution_time)
                VALUES (?, ?, ?, ?)
            ''', (function_name, action_type, datetime.now().isoformat(), execution_time))
            conn.commit()

    def compare_with_average(self, function_name, current_duration):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT execution_time FROM events
                WHERE function_name = ? AND action_type = 'end'
            ''', (function_name,))
            times = cursor.fetchall()
            if times and len(times) > 1:
                average_duration = sum(t[0] for t in times if t[0] is not None) / len(times)
                deviation = ((current_duration - average_duration) / average_duration) * 100
                color = "\033[91m" if deviation > 0 else "\033[92m"
                print(f"{color}This time it took {abs(deviation):.2f}% {'more' if deviation > 0 else 'less'} than the average.\033[0m")

def track_function(func):
    return FunctionTracker(func)
