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
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS table_projects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE,
                    rank INTEGER
                );
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS table_project_steps (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    project_id INTEGER,
                    sequence INTEGER,
                    name TEXT,
                    FOREIGN KEY(project_id) REFERENCES table_projects(id) ON DELETE CASCADE
                );
            ''')
            conn.commit()

    def start_new_project(self, project_name, first_step):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE table_projects SET rank = rank + 1")
            cursor.execute("INSERT INTO table_projects (name, rank) VALUES (?, 1)", (project_name,))
            project_id = cursor.lastrowid
            cursor.execute("INSERT INTO table_project_steps (project_id, sequence, name) VALUES (?, 1, ?)", (project_id, first_step))
            conn.commit()
            print("New project started with initial step.")
            return True

    def delete_project(self, project_id):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM table_projects WHERE id=?", (project_id,))
            cursor.execute("UPDATE table_projects SET rank = rank - 1 WHERE rank > (SELECT rank FROM table_projects WHERE id=?)", (project_id,))
            conn.commit()
            print(f"Project with ID {project_id} and all related steps have been deleted.")

    def make_progress(self, project="intelligent_random"):
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

    def _get_project_id(self, cursor, project):
        if project == "intelligent_random":
            cursor.execute("SELECT id, rank FROM table_projects")
            projects = cursor.fetchall()
            if not projects:
                print("No ongoing projects found.")
                return None
            weights = [1 / p[1] for p in projects]
            total_weight = sum(weights)
            normalized_weights = [w / total_weight for w in weights]
            selected_project = random.choices(projects, weights=normalized_weights, k=1)[0]
            return selected_project[0]
        else:
            cursor.execute("SELECT id FROM table_projects WHERE name=?", (project,))
            result = cursor.fetchone()
            if not result:
                print("Project not found.")
                return None
            return result[0]

    def _get_latest_step(self, cursor, project_id):
        cursor.execute("SELECT id, sequence, name FROM table_project_steps WHERE project_id=? ORDER BY sequence DESC LIMIT 1", (project_id,))
        return cursor.fetchone()

    def _handle_project_progress(self, cursor, project_id, sequence):
        while True:
            response = input("Enter 'continue' to proceed or 'end project' to finish: ").lower()
            if response == 'continue':
                next_step = input("Enter the next step: ")
                sequence += 1
                cursor.execute("INSERT INTO table_project_steps (project_id, sequence, name) VALUES (?, ?, ?)", (project_id, sequence, next_step))
                break
            elif response == 'end project':
                self.delete_project(project_id)
                break
            else:
                print("Invalid answer. Please try again.")

    def project_exists(self, project_name):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM table_projects WHERE name=?", (project_name,))
            exists = cursor.fetchone()
            return exists is not None
