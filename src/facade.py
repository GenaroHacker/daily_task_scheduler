import json
import os
from datetime import datetime
from src.director import Director
from src.facade_modules.theme import SeasonThemeManager
from src.facade_modules.annual_events import AnnualEventManager


class Facade:
    """
    A class to manage the execution of scheduled tasks on a daily basis,
    with each day potentially having a different set of tasks.
    Tasks are executed only once per day and the state is saved using JSON.

    Attributes:
        schedule (dict): A dictionary mapping weekdays (0-6) to lists of function identifiers.
        functions (dict): A dictionary mapping function identifiers to function objects.
        state_file (str): The filename where the execution state is stored.
    """

    def __init__(self, schedule, functions):
        """
        Initializes the DailyTaskScheduler with a specific schedule and set of functions.

        Parameters:
            schedule (dict): Weekday to function keys mapping.
            functions (dict): Function keys to functions mapping.
        """
        self.schedule = schedule
        self.functions = functions
        self.state_file = os.path.join("assets", "data", "state.json")
        os.makedirs(os.path.dirname(self.state_file), exist_ok=True)

        # Check if all items in the schedule values are included in the functions keys
        for day, tasks in self.schedule.items():
            for task in tasks:
                if task not in self.functions:
                    raise ValueError(f"Task '{task}' in schedule for '{day}' is not defined in functions dictionary.")


    def _update_state(self, index):
        """
        Updates the execution state by writing the last executed index and date to a JSON file.

        Parameters:
            index (int): The index of the last executed function in the daily schedule.
        """
        state_data = {
            "last_executed_index": index,
            "date": datetime.now().date().isoformat(),
        }
        with open(self.state_file, "w") as file:
            json.dump(state_data, file)

    def _get_last_state(self):
        """
        Retrieves the last execution state from a JSON file.

        Returns:
            int or None: The index of the last executed function if the execution was on the current day, otherwise None.
        """
        try:
            with open(self.state_file, "r") as file:
                state_data = json.load(file)
                if state_data["date"] == datetime.now().date().isoformat():
                    return state_data["last_executed_index"]
        except FileNotFoundError:
            return None

    def reset_state(self):
        """
        Resets the execution state by removing the state file.
        """
        if os.path.exists(self.state_file):
            os.remove(self.state_file)

    def execute_instructions(self):
        """
        Executes the scheduled tasks for the current day.
        Ensures tasks are not repeated if they have been executed earlier the same day.
        """
        d = Director()
        day_names = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        today = day_names[datetime.now().weekday()]
        if today in self.schedule:
            functions_today = self.schedule[today]
            last_executed_index = self._get_last_state()

            if (
                last_executed_index is not None
                and last_executed_index >= len(functions_today) - 1
            ):
                print("All tasks for today have been completed.")
                return

            start_index = (
                last_executed_index + 1 if last_executed_index is not None else 0
            )

            SeasonThemeManager().manage_theme()
            AnnualEventManager().print_upcoming_events()
            d.input()

            for index, function_key in enumerate(
                functions_today[start_index:], start=start_index
            ):
                self.functions[function_key]()  # Execute the function using key
                self._update_state(index)  # Update state after execution
