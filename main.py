from src.facade import Facade


from smark.task_functions.practice import pomodoro_session

from smark.task_functions.recreate import coffee
from smark.task_functions.recreate import breathing_exercise

from smark.task_functions.create import organize_desk
from smark.task_functions.create import organize_digital_files
from smark.task_functions.create import get_things_done
from smark.task_functions.create import make_progress
from smark.task_functions.create import rank_projects


if __name__ == '__main__':
    # Map functions to function keys
    functions = {
        'coffee': coffee,
        'desk': organize_desk,
        'files': organize_digital_files,
        'pomodoro': pomodoro_session,
        'gtd': get_things_done,
        'progress': make_progress,
        'rank': rank_projects,
        'breath': breathing_exercise
    }

    # Define weekly schedule using function keys
    weekly_schedule = {
        0: ['gtd', 'rank'],         # Monday
        1: ['coffee', 'breath'],    # Tuesday
        2: ['coffee', 'files', 'gtd'],     # Wednesday
        3: ['coffee', 'desk'],      # Thursday
        4: ['coffee', 'desk'],      # Friday
        5: ['coffee', 'pomodoro'],  # Saturday
        6: ['coffee', 'gtd']        # Sunday
    }

    scheduler = Facade(weekly_schedule, functions)
    scheduler.execute_instructions()
