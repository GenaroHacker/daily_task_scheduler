from src.scheduler import DailyTaskScheduler

from task_functions.create import organize_desk
from task_functions.create import organize_digital_files
from task_functions.recreate import coffee
from task_functions.practice import pomodoro_session


if __name__ == '__main__':
    # Map functions to function keys
    functions = {
        'coffee': coffee,
        'desk': organize_desk,
        'files': organize_digital_files,
        'pomodoro': pomodoro_session
    }

    # Define weekly schedule using function keys
    weekly_schedule = {
        0: ['coffee', 'desk'],      # Monday
        1: ['coffee', 'files'],     # Tuesday
        2: ['coffee', 'files'],     # Wednesday
        3: ['coffee', 'desk'],      # Thursday
        4: ['coffee', 'desk'],      # Friday
        5: ['coffee', 'pomodoro'],  # Saturday
        6: ['coffee', 'files']      # Sunday
    }

    scheduler = DailyTaskScheduler(weekly_schedule, functions)
    scheduler.execute_instructions()
