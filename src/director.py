import os
import subprocess
import random
import sqlite3
from time import sleep
import sys
import time

class Director:
    DB_PATH = os.path.join('assets', 'data', 'projects.db')
    SOUNDS_DIR = os.path.join('assets', 'sounds')
    SCRIPTS_DIR = os.path.join('assets', 'scripts')

    def __init__(self):
        self._create_db_if_not_exists()

    def _create_db_if_not_exists(self):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS table_projects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE,
                    is_finished BOOLEAN DEFAULT 0
                );
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS table_project_steps (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    project_id INTEGER,
                    sequence INTEGER,
                    name TEXT,
                    FOREIGN KEY(project_id) REFERENCES table_projects(id)
                );
            ''')
            conn.commit()

    def _execute_command(self, command, shell=False):
        try:
            subprocess.run(command, shell=shell, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Command failed: {e}")

    def sleep(self, minutes=0, seconds=0):
        total_seconds = minutes * 60 + seconds
        interval = total_seconds / 40  # Compute the interval for updating the progress bar

        for i in range(1, 41):
            time.sleep(interval)
            progress = '#' * i  # Completed portion
            remaining = '-' * (40 - i)  # Pending portion
            sys.stdout.write('\r[{}]'.format(progress + remaining))  # Overwrite the current line
            sys.stdout.flush()

        print()  # Move to the next line after completion

    def clear(self):
        self._execute_command('clear', shell=True)

    def run_sh_script(self, script_name):
        script_path = os.path.join(self.SCRIPTS_DIR, script_name)
        self._execute_command(['/bin/bash', script_path])

    def execute_sh_command(self, command):
        self._execute_command(command, shell=True)

    def open_file(self, program, file_name):
        file_path = os.path.abspath(file_name)
        self._execute_command([program, file_path])

    def open_webpage(self, url):
        self._execute_command(['xdg-open', url])

    def play_sound(self, sound="beeps.wav"):
        sound_path = os.path.join(self.SOUNDS_DIR, sound)
        self._execute_command(['aplay', sound_path])

    def start_new_project(self, project_name, first_step):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            # Check if project already exists to prevent duplicates
            cursor.execute("SELECT id FROM table_projects WHERE name=?", (project_name,))
            if cursor.fetchone() is not None:
                print("Project already exists.")
                return False
            
            # Insert new project into table_projects
            cursor.execute("INSERT INTO table_projects (name) VALUES (?)", (project_name,))
            project_id = cursor.lastrowid  # Retrieve the ID of the newly created project

            # Insert the first step into table_project_steps
            cursor.execute("INSERT INTO table_project_steps (project_id, sequence, name) VALUES (?, 1, ?)", (project_id, first_step))
            conn.commit()
            print("New project started with the initial step.")
            return True

    def make_progress(self, project="random"):
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
        if project == "random":
            cursor.execute("SELECT id FROM table_projects WHERE is_finished=0")
            projects = cursor.fetchall()
            if not projects:
                print("No ongoing projects found.")
                return None
            return random.choice(projects)[0]
        else:
            cursor.execute("SELECT id FROM table_projects WHERE name=? AND is_finished=0", (project,))
            result = cursor.fetchone()
            if not result:
                print("Project not found or already completed.")
                return None
            return result[0]

    def _get_latest_step(self, cursor, project_id):
        cursor.execute("SELECT id, sequence, name FROM table_project_steps WHERE project_id=? ORDER BY sequence DESC LIMIT 1", (project_id,))
        return cursor.fetchone()

    def _handle_project_progress(self, cursor, project_id, sequence):
        while True:  # Start an indefinite loop to keep asking until valid input is provided
            response = input("Enter 'continue' to proceed or 'end project' to finish: ").lower()
            
            if response == 'continue':
                next_step = input("Enter the next step: ")
                sequence += 1
                cursor.execute("INSERT INTO table_project_steps (project_id, sequence, name) VALUES (?, ?, ?)", (project_id, sequence, next_step))
                break  # Exit the loop after valid processing
            elif response == 'end project':
                cursor.execute("UPDATE table_projects SET is_finished=1 WHERE id=?", (project_id,))
                print("Project completed.")
                break  # Exit the loop after completing the project
            else:
                print("Invalid answer. Please try again.")  # Inform the user and repeat the loop


if __name__ == '__main__':
    director = Director()
    director.clear()
    director.sleep(seconds=5)
    director.play_sound()
    director.run_sh_script('example.sh')
    director.open_webpage("http://example.com")
    director.execute_sh_command('ls')
    director.start_new_project('Sample Project', 'Initial Setup')
    director.make_progress('Sample Project')
