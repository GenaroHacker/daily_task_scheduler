# The core functions are not self-contained.
# They implement functionality beyond the basic director class methods.
# To understand their operations, refer to the other parts of the program they depend on.


from src.director import Director
from src.decorator import track_function
from task_functions.func_modules.gtd import GettingThingsDone
from task_functions.func_modules.list import IdeaManager
from task_functions.func_modules.patterns import implement_design_pattern
from task_functions.func_modules.coffee import Coffee


d = Director()


@track_function
def get_things_done(db_path="assets/data/smark.db"):
    gtd = GettingThingsDone(db_path)
    new_project_added = gtd.run()
    # rank projects only if new projects were added
    if new_project_added:
        gtd.d.rank_projects()


@track_function
def make_progress():
    d.make_progress()


@track_function
def list_ideas():
    db_path = "assets/data/smark.db"
    manager = IdeaManager(db_path)
    manager.run()


@track_function
def implement_gof_pattern():
    implement_design_pattern()


@track_function
def plot_metrics():
    d.plot_time_worked()
    d.plot_event_schedule()
    d.plot_start_and_end_hours()
    d.plot_task_time_distribution()
    d.plot_work_vs_break_time_distribution()
    d.plot_daily_skipped_vs_completed_tasks()


@track_function
def coffee():
    coffee_routine = Coffee(d)
    coffee_routine.execute()

