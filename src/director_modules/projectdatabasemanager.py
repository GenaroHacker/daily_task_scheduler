import sqlite3
import os
import random

class ProjectDatabaseManager:
    DB_PATH = os.path.join('assets', 'data', 'projects.db')

    def __init__(self):
        self._create_db_if_not_exists()

    def _create_db_if_not_exists(self):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS table_projects (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE, is_finished BOOLEAN DEFAULT 0);''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS table_project_steps (id INTEGER PRIMARY KEY AUTOINCREMENT, project_id INTEGER, sequence INTEGER, name TEXT, FOREIGN KEY(project_id) REFERENCES table_projects(id));''')
            conn.commit()

    def start_new_project(self, project_name, first_step):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM table_projects WHERE name=?", (project_name,))
            if cursor.fetchone() is not None:
                print("Project already exists.")
                return False

            cursor.execute("INSERT INTO table_projects (name) VALUES (?)", (project_name,))
            project_id = cursor.lastrowid
            cursor.execute("INSERT INTO table_project_steps (project_id, sequence, name) VALUES (?, 1, ?)", (project_id, first_step))
            conn.commit()
            print("New project started with the initial step.")
            return True

    def make_progress(self, project):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            project_id = self._get_project_id(cursor, project)
            if not project_id:
                return

            step = self._get_latest_step(cursor, project_id)
            if not step:
                print("No steps found for this project.")
                return

            step_id, sequence, step_name = step
            print(f"Step {sequence}: {step_name}")
            self._handle_project_progress(cursor, project_id, sequence)
