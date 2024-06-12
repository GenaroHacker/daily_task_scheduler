from src.director import Director
import sqlite3
from datetime import datetime

class GettingThingsDone:
    def __init__(self, db_path):
        self.db_path = db_path
        self.items = []
        self.actionables = []
        self.non_actionables = []
        self.quick_tasks = []
        self.long_tasks_today = []
        self.long_tasks_future = []
        self.reference_materials = []
        self.trash = []
        self.d = Director()
        self.initialize_database()

    def initialize_database(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS refs
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, reference TEXT)"""
        )
        conn.commit()
        conn.close()

    def input_yes_no(self, prompt):
        while True:
            response = input(prompt).lower()
            if response in ["y", "n"]:
                return response == "y"
            self.d.print("Please enter 'y' for yes or 'n' for no.")

    def capture_items(self):
        self.d.print(
            "Enter all items on your mind one by one. Type 'end' when you are finished capturing."
        )
        while True:
            item = input("Enter an item: ")
            if item.lower() == "end":
                break
            if item and item not in self.items:
                self.items.append(item)

    def categorize_items(self):
        self.d.clear()
        for item in self.items:
            if self.input_yes_no(f"Is the item '{item}' actionable? (y/n): "):
                self.actionables.append(item)
            else:
                self.non_actionables.append(item)

    def determine_next_steps(self):
        self.d.clear()
        new_project_added = False
        if self.actionables:
            for item in self.actionables:
                if item in self.quick_tasks:
                    continue
                if self.d.project_exists(item):
                    print(f"Project '{item}' already exists. Skipping...")
                else:
                    if self.input_yes_no(f"Does the item '{item}' need to be finished today? (y/n): "):
                        self.long_tasks_today.append(item)
                    else:
                        self.long_tasks_future.append(item)
                        new_project_added = True
        return new_project_added

    def process_quick_tasks(self):
        self.d.clear()
        for item in self.actionables:
            if self.input_yes_no(
                f"Does the item '{item}' take less than 2 minutes to complete? (y/n): "
            ):
                self.quick_tasks.append(item)

    def process_non_actionables(self):
        self.d.clear()
        for item in self.non_actionables:
            if self.input_yes_no(
                f"Do you want to keep the item '{item}' as reference? (y/n): "
            ):
                self.reference_materials.append(item)
            else:
                self.trash.append(item)

    def save_references(self):
        if not self.reference_materials:
            self.d.print("No reference materials to save.")
            return
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        for reference in self.reference_materials:
            cursor.execute("INSERT INTO refs (reference) VALUES (?)", (reference,))
        conn.commit()
        conn.close()
        self.d.print("Reference materials saved.")

    def execute_quick_tasks(self):
        self.d.clear()
        if not self.quick_tasks:
            self.d.print("No quick tasks to perform.")
            return
        self.d.print("Quick tasks to do now (less than 2 minutes):")
        for quick_task in self.quick_tasks:
            self.d.print(f"- {quick_task}")
            self.d.input()

    def review_references(self):
        self.d.clear()
        self.d.print("Review your saved references:")
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, reference FROM refs ORDER BY id ASC")
        refs = cursor.fetchall()
        if not refs:
            self.d.print("No references to display.")
            return
        while True:
            for idx, (ref_id, ref) in enumerate(refs, start=1):
                self.d.print(f"[ {ref_id} ] {ref}")
            choice = input(
                "Type a reference ID to update/delete, or type 'end' to finish: "
            )
            if choice.lower() == "end":
                break
            if choice.isdigit() and any(ref_id == int(choice) for ref_id, _ in refs):
                action = input(
                    "Type 'update' to update or 'delete' to delete the reference: "
                )
                if action.lower() == "update":
                    new_ref = input("Enter the new reference: ")
                    cursor.execute(
                        "UPDATE refs SET reference = ? WHERE id = ?", (new_ref, choice)
                    )
                    conn.commit()
                    self.d.print("Reference updated.")
                elif action.lower() == "delete":
                    cursor.execute("DELETE FROM refs WHERE id = ?", (choice,))
                    cursor.execute(
                        "UPDATE refs SET id = id - 1 WHERE id > ?", (choice,)
                    )
                    conn.commit()
                    self.d.print("Reference deleted.")
                # Refresh the list after update or delete
                refs = cursor.execute(
                    "SELECT id, reference FROM refs ORDER BY id ASC"
                ).fetchall()
                self.d.clear()
            else:
                self.d.print("Invalid ID. Please try again.")
                self.d.clear()

    def display_long_tasks_today(self):
        self.d.clear()
        if not self.long_tasks_today:
            self.d.print("No tasks to be finished today.")
            return
        self.d.print("Tasks to be finished today:")
        for task in self.long_tasks_today:
            self.d.print(f"- {task}")
        current_date = datetime.now().strftime("%A, %Y-%m-%d")
        self.d.print(f"Write these down as a checklist on the whiteboard. Today's date is {current_date}. Use this as the title of the checklist.")
        self.d.input()

    def run(self):
        self.capture_items()
        self.categorize_items()
        self.process_quick_tasks()
        new_project_added = self.determine_next_steps()
        self.process_non_actionables()
        self.save_references()
        self.execute_quick_tasks()
        self.review_references()
        self.display_long_tasks_today()
        self.d.clear()
        self.d.print("Tasks to discard as trash:")
        for discarded in self.trash:
            self.d.print(f"- {discarded}")
        self.d.clear()
        return new_project_added
