import sqlite3
import os
import random
from datetime import datetime


class ProjectDatabaseManager:
    DB_PATH = os.path.join("assets", "data", "smark.db")

    def __init__(self):
        self._create_db_if_not_exists()

    def _create_db_if_not_exists(self):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            # Create projects and project steps tables
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS table_projects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE,
                    rank INTEGER
                );
            """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS table_project_steps (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    project_id INTEGER,
                    timestamp DATETIME,
                    name TEXT,
                    FOREIGN KEY(project_id) REFERENCES table_projects(id) ON DELETE CASCADE
                );
            """
            )
            # Create archived projects and project steps tables
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS table_projects_archived (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE
                );
            """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS table_project_steps_archived (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    project_id INTEGER,
                    timestamp DATETIME,
                    name TEXT,
                    FOREIGN KEY(project_id) REFERENCES table_projects_archived(id) ON DELETE CASCADE
                );
            """
            )
            conn.commit()

    def start_new_project(self, project_name, first_step):
        timestamp = datetime.now()
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE table_projects SET rank = rank + 1")
            cursor.execute(
                "INSERT INTO table_projects (name, rank) VALUES (?, 1)", (project_name,)
            )
            project_id = cursor.lastrowid
            cursor.execute(
                "INSERT INTO table_project_steps (project_id, timestamp, name) VALUES (?, ?, ?)",
                (project_id, timestamp, first_step),
            )
            conn.commit()
            print("New project started with initial step.")
            return True

    def delete_project(self, project_id):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            conn.execute("BEGIN TRANSACTION;")
            try:
                # Archive the project
                project_details = cursor.execute(
                    "SELECT name FROM table_projects WHERE id=?", (project_id,)
                ).fetchone()
                if project_details:
                    cursor.execute(
                        "INSERT INTO table_projects_archived (name) VALUES (?)",
                        (project_details[0],),
                    )
                    archive_id = cursor.lastrowid
                    steps = cursor.execute(
                        "SELECT timestamp, name FROM table_project_steps WHERE project_id=?",
                        (project_id,),
                    ).fetchall()
                    for step in steps:
                        cursor.execute(
                            "INSERT INTO table_project_steps_archived (project_id, timestamp, name) VALUES (?, ?, ?)",
                            (archive_id, step[0], step[1]),
                        )

                # Step 1: Explicitly delete all steps in table_project_steps with the project_id
                cursor.execute(
                    "DELETE FROM table_project_steps WHERE project_id=?", (project_id,)
                )

                # Step 2: Get the rank of the project to be deleted
                rank_to_delete = cursor.execute(
                    "SELECT rank FROM table_projects WHERE id=?", (project_id,)
                ).fetchone()
                if rank_to_delete:
                    rank_to_delete = rank_to_delete[0]
                    cursor.execute(
                        "UPDATE table_projects SET rank = rank - 1 WHERE rank > ?",
                        (rank_to_delete,),
                    )

                # Step 3: Delete the project record
                cursor.execute("DELETE FROM table_projects WHERE id=?", (project_id,))

                # Step 4: Update the IDs of the projects with higher IDs
                higher_projects = cursor.execute(
                    "SELECT id FROM table_projects WHERE id > ?", (project_id,)
                ).fetchall()
                for (higher_id,) in higher_projects:
                    new_id = higher_id - 1
                    cursor.execute(
                        "UPDATE table_project_steps SET project_id=? WHERE project_id=?",
                        (new_id, higher_id),
                    )
                    cursor.execute(
                        "UPDATE table_projects SET id=? WHERE id=?", (new_id, higher_id)
                    )

                # Commit changes
                conn.commit()
                print(
                    f"Project with ID {project_id} and all related steps have been archived and deleted."
                )
            except sqlite3.Error as e:
                # Roll back any changes if an error occurs
                conn.rollback()
                print(f"An error occurred: {e}")

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
            selected_project = random.choices(
                projects, weights=normalized_weights, k=1
            )[0]
            return selected_project[0]
        else:
            cursor.execute("SELECT id FROM table_projects WHERE name=?", (project,))
            result = cursor.fetchone()
            if not result:
                print("Project not found.")
                return None
            return result[0]

    def _get_latest_step(self, cursor, project_id):
        cursor.execute(
            "SELECT id, timestamp, name FROM table_project_steps WHERE project_id=? ORDER BY timestamp DESC LIMIT 1",
            (project_id,),
        )
        return cursor.fetchone()

    def make_progress(self, project="intelligent_random"):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            project_id = self._get_project_id(cursor, project)
            if not project_id:
                print("No project found.")
                return

            project_name = cursor.execute(
                "SELECT name FROM table_projects WHERE id=?", (project_id,)
            ).fetchone()[0]
            print(f"Project: {project_name}")

            step = self._get_latest_step(cursor, project_id)
            if not step:
                print("No steps found for this project.")
                return

            step_id, timestamp, step_name = step
            print(f"Latest step on {timestamp}: {step_name}")

            self._handle_project_progress(cursor, project_id)

    def _handle_project_progress(self, cursor, project_id):
        while True:
            response = input(
                "Enter 'continue' to proceed or 'end project' to finish: "
            ).lower()
            if response == "continue":
                next_step = input("Enter the next step: ")
                timestamp = datetime.now()
                cursor.execute(
                    "INSERT INTO table_project_steps (project_id, timestamp, name) VALUES (?, ?, ?)",
                    (project_id, timestamp, next_step),
                )
                print(f"Step added: {next_step} at {timestamp}")
                break
            elif response == "end project":
                self.delete_project(project_id)
                print("Project has been ended and deleted.")
                break
            else:
                print("Invalid answer. Please try again.")

    def project_exists(self, project_name):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM table_projects WHERE name=?", (project_name,))
            exists = cursor.fetchone()
            return exists is not None

    def rank_projects(self):
        def ask_user_cmp(item1, item2):
            while True:
                print(f" [ 1 ] [{item1}] ?")
                print(f" [ 2 ] [{item2}] ?")
                cmp = input(" --> ? ")
                if cmp == "1":
                    return -1  # Higher priority for item1
                if cmp == "2":
                    return 1  # Higher priority for item2
                print("1 or 2, please!")

        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name FROM table_projects ORDER BY rank")
            projects = cursor.fetchall()
            project_names = [p[1] for p in projects]

            # Use sorted with a comparison function via functools.cmp_to_key
            from functools import cmp_to_key

            sorted_projects = sorted(project_names, key=cmp_to_key(ask_user_cmp))

            # Update the database with new rankings
            for rank, project_name in enumerate(sorted_projects, start=1):
                cursor.execute(
                    "UPDATE table_projects SET rank = ? WHERE name = ?",
                    (rank, project_name),
                )

            conn.commit()
            print("Projects have been successfully re-ranked based on user input.")
