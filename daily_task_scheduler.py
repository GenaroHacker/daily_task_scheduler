import pickle
import os
from datetime import datetime

class DailyTaskScheduler:
    def __init__(self, schedule, functions):
        self.schedule = schedule
        self.functions = functions
        self.state_file = "state.pkl"  # File to store the state

    def update_state(self, index):
        state_data = {
            'last_executed_index': index,
            'date': datetime.now().date().isoformat()
        }
        with open(self.state_file, "wb") as file:
            pickle.dump(state_data, file)

    def get_last_state(self):
        try:
            with open(self.state_file, "rb") as file:
                state_data = pickle.load(file)
                if state_data['date'] == datetime.now().date().isoformat():
                    return state_data['last_executed_index']
        except FileNotFoundError:
            return None

    def reset_state(self):
        if os.path.exists(self.state_file):
            os.remove(self.state_file)

    def execute_instructions(self):
        today = datetime.now().weekday()
        if today in self.schedule:
            functions_today = self.schedule[today]
            last_executed_index = self.get_last_state()

            if last_executed_index is not None and last_executed_index >= len(functions_today) - 1:
                print("All tasks for today have been completed.")
                return
            
            start_index = last_executed_index + 1 if last_executed_index is not None else 0

            for index, function_key in enumerate(functions_today[start_index:], start=start_index):
                self.functions[function_key]()  # Execute the function using key
                self.update_state(index)  # Update state after execution

if __name__ == "__main__":
    # Define functions
    def function_A():
        print("Executing function A")

    def function_B():
        print("Executing function B")

    def function_C():
        print("Executing function C")

    def function_D():
        print("Executing function D")

    def function_E():
        print("Executing function E")

    # Map functions to function keys
    functions = {
        'A': function_A,
        'B': function_B,
        'C': function_C,
        'D': function_D,
        'E': function_E
    }

    # Define weekly schedule using function keys
    weekly_schedule = {
        0: ['A', 'B'],  # Monday
        1: ['C'],       # Tuesday
        2: ['A', 'C'],  # Wednesday
        3: ['D', 'E'],  # Thursday
        4: ['B', 'E'],  # Friday
        5: ['A'],       # Saturday
        6: ['E']        # Sunday
    }

    scheduler = DailyTaskScheduler(weekly_schedule, functions)
    scheduler.execute_instructions()
