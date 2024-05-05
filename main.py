from src.director import Director
from src.scheduler import DailyTaskScheduler
from src.decorator import track_function

from task_functions.create import organize_desk
from task_functions.create import organize_digital_files
from task_functions.recreate import coffee
from task_functions.practice import pomodoro_session


if __name__ == '__main__':
    #d = Director()
    #d.clear()
    #d.sleep(seconds=0.1)
    #d.play_sound()
    #d.run_script('example.sh')
    #d.open_webpage("http://example.com")
    #d.execute_command('ls')
    #d.start_new_project('Sample Project', 'Initial Setup')
    #d.make_progress('Sample Project')
    #d.print("Hello, world! This is an example with a very long sentence to test line breaking without cutting words short. Enjoy reading slowly.\nNew lines are properly handled with adaptive delay.")
    

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