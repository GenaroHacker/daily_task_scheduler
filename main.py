from src.facade import Facade


# Practice
from task_functions.practice import pomodoro_session
from task_functions.practice import guitar_loop_note
from task_functions.practice import solve_leetcode_problem
from task_functions.practice import practice_fast_typing
from task_functions.practice import practice_calligraphy
from task_functions.practice import take_exam
from task_functions.practice import implement_design_pattern

# Exercise
from task_functions.exercise import go_to_gym
from task_functions.exercise import do_40_pushups

# Recreate
from task_functions.recreate import coffee
from task_functions.recreate import breathing_exercise
from task_functions.recreate import plot_metrics
from task_functions.recreate import eat
from task_functions.recreate import get_a_shower
from task_functions.recreate import shave_face
from task_functions.recreate import brush_teeth
from task_functions.recreate import take_supplements
from task_functions.recreate import drink_water
from task_functions.recreate import practice_meditation

# Create
from task_functions.create import organize_desk
from task_functions.create import organize_digital_files
from task_functions.create import get_things_done
from task_functions.create import make_progress
from task_functions.create import rank_projects
from task_functions.create import transcribe_highlighted_text
from task_functions.create import list
from task_functions.create import make_the_bed
from task_functions.create import prepare_tomorrow_clothes
from task_functions.create import clean_room
from task_functions.create import washing_machine



if __name__ == "__main__":
    # Map functions to function keys
    functions = {
        "coffee": coffee,
        "desk": organize_desk,
        "files": organize_digital_files,
        "pomodoro": pomodoro_session,
        "gtd": get_things_done,
        "progress": make_progress,
        "rank": rank_projects,
        "breath": breathing_exercise,
        "plot": plot_metrics,
        "eat": eat,
        "gym": go_to_gym,
        "pushups": do_40_pushups,
        "loop": guitar_loop_note,
        "leetcode": solve_leetcode_problem,
        "list": list,
        "typing": practice_fast_typing,
        "calligraphy": practice_calligraphy,
        "exam": take_exam,
        "design": implement_design_pattern,
        "shower": get_a_shower,
        "shave": shave_face,
        "brush": brush_teeth,
        "supplements": take_supplements,
        "water": drink_water,
        "meditation": practice_meditation,
        "transcribe": transcribe_highlighted_text,
        "bed": make_the_bed,
        "clothes": prepare_tomorrow_clothes,
        "clean": clean_room,
        "wash": washing_machine
    }

    wake_up = ["water", "shower", "water", "coffee", "desk", "plot", "gtd", "rank", "water", "pomodoro", "water", "progress", "water"]
    ending = ["eat","water", "vitamins", "plot", "shave", "brush"]

    # Define weekly schedule using function keys
    weekly_schedule = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": ["coffee"],
        "Friday": [],
        "Saturday": [],
        "Sunday": []
    }

    scheduler = Facade(weekly_schedule, functions)
    scheduler.execute_instructions()
