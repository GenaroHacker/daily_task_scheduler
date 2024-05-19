from src.facade import Facade


from task_functions.practice import pomodoro_session
from task_functions.practice import guitar_loop_note
from task_functions.practice import solve_leetcode_problem

from task_functions.exercise import go_to_gym
from task_functions.exercise import do_40_pushups

from task_functions.recreate import coffee
from task_functions.recreate import breathing_exercise
from task_functions.recreate import plot_metrics
from task_functions.recreate import eat

from task_functions.create import organize_desk
from task_functions.create import organize_digital_files
from task_functions.create import get_things_done
from task_functions.create import make_progress
from task_functions.create import rank_projects


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
        'breath': breathing_exercise,
        'plot': plot_metrics,
        'eat': eat,
        'gym': go_to_gym,
        'pushups': do_40_pushups,
        'loop': guitar_loop_note,
        'leetcode': solve_leetcode_problem
    }


    # Define weekly schedule using function keys
    weekly_schedule = {
        "Monday": ['gtd', 'rank'],
        "Tuesday": ['coffee', 'breath'],
        "Wednesday": ['plot', 'coffee', 'files', 'gtd'],
        "Thursday": ['plot', 'coffee', 'desk'],
        "Friday": ['plot', 'desk'],
        "Saturday": ['plot', 'pomodoro'],
        "Sunday": ['leetcode', 'loop']
    }

    scheduler = Facade(weekly_schedule, functions)
    scheduler.execute_instructions()
