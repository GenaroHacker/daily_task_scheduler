import os
import sqlite3
from datetime import datetime, timedelta
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

class AnnualEventManager:
    DB_PATH = os.path.join('assets', 'data', 'smark.db')

    def __init__(self):
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS annual_events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    event TEXT,
                    month INT,
                    day INT
                );
            ''')
            conn.commit()

    def review_events(self):
        while True:
            with sqlite3.connect(self.DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, event, month, day FROM annual_events ORDER BY month, day")
                events = cursor.fetchall()

            print("List of all events:")
            for event in events:
                print(f"[ {event[0]} ] {event[1]} | {event[2]:02}-{event[3]:02}")

            choice = input("Enter an event ID to update or delete, 'add' to add a new event, or 'end' to finish: ").strip().lower()
            if choice == 'add':
                self._add_event()
            elif choice == 'end':
                break
            elif choice.isdigit() and int(choice) in [event[0] for event in events]:
                self._event_menu(int(choice))
            else:
                print("Invalid input, please try again.")

    def _add_event(self):
        while True:
            event_name = input("Enter the name of the event: ")
            month = input("Enter the month of the event (1-12 or full month name): ").strip()
            day = input("Enter the day of the event: ").strip()

            month = self._parse_month(month)
            if month is None or not day.isdigit() or not 1 <= int(day) <= 31:
                print("Invalid date, please try again.")
                continue

            with sqlite3.connect(self.DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO annual_events (event, month, day) VALUES (?, ?, ?)", (event_name, month, int(day)))
                conn.commit()
            print("Event added successfully.")
            break

    def _parse_month(self, month):
        try:
            return int(month) if month.isdigit() else datetime.strptime(month, '%B').month
        except ValueError:
            try:
                return datetime.strptime(month.capitalize(), '%B').month
            except ValueError:
                return None

    def _event_menu(self, event_id):
        while True:
            print(f"Selected event ID: [ {event_id} ]")
            choice = input("Choose an option: [1] Update, [2] Delete, [3] Go back: ").strip()

            if choice == '1':
                self._update_event(event_id)
            elif choice == '2':
                self._delete_event(event_id)
                break
            elif choice == '3':
                break
            else:
                print("Invalid input, please try again.")

    def _update_event(self, event_id):
        while True:
            choice = input("Choose an option: [1] Update name, [2] Update date, [3] Go back: ").strip()

            if choice == '1':
                new_name = input("Enter the new name for the event: ")
                with sqlite3.connect(self.DB_PATH) as conn:
                    cursor = conn.cursor()
                    cursor.execute("UPDATE annual_events SET event = ? WHERE id = ?", (new_name, event_id))
                    conn.commit()
                print("Event name updated successfully.")
                break
            elif choice == '2':
                new_month = input("Enter the new month (1-12 or full month name): ").strip()
                new_day = input("Enter the new day: ").strip()

                new_month = self._parse_month(new_month)
                if new_month is None or not new_day.isdigit() or not 1 <= int(new_day) <= 31:
                    print("Invalid date, please try again.")
                    continue

                with sqlite3.connect(self.DB_PATH) as conn:
                    cursor = conn.cursor()
                    cursor.execute("UPDATE annual_events SET month = ?, day = ? WHERE id = ?", (new_month, int(new_day), event_id))
                    conn.commit()
                print("Event date updated successfully.")
                break
            elif choice == '3':
                break
            else:
                print("Invalid input, please try again.")

    def _delete_event(self, event_id):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM annual_events WHERE id = ?", (event_id,))
            conn.commit()
        print("Event deleted successfully.")

    def print_upcoming_events(self, date_range=(-5, 30)):
        today = datetime.now()
        start_date = today + timedelta(days=date_range[0])
        end_date = today + timedelta(days=date_range[1])

        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT event, month, day FROM annual_events")
            events = cursor.fetchall()

        print("Upcoming events:")
        for event in events:
            event_date = datetime(today.year, event[1], event[2])
            delta_days = (event_date - today).days

            if start_date <= event_date <= end_date:
                if delta_days < 0:
                    color = Fore.RED
                elif delta_days == 0:
                    color = Fore.YELLOW
                else:
                    color = Fore.GREEN

                date_str = "yesterday" if delta_days == -1 else "today" if delta_days == 0 else "tomorrow" if delta_days == 1 else event_date.strftime("%m-%d")
                print(f"{color}{event[0]:20} | {date_str}")

