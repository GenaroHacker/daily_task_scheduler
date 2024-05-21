from src.director_modules.metrics.time_worked import plot_time_worked
from src.director_modules.metrics.worked_hours import plot_start_and_end_hours
from src.director_modules.metrics.time_charts import plot_task_time_distribution
from src.director_modules.metrics.break_time import plot_work_vs_break_time_distribution
from src.director_modules.metrics.bar_skipped import (
    plot_daily_skipped_vs_completed_tasks,
)
from src.director_modules.metrics.tasks_completed import plot_event_schedule


class Plotter:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def plot_time_worked(self, days_range: int = None) -> None:
        plot_time_worked(self.db_path, days_range)

    def plot_start_and_end_hours(self, days_range: int = None) -> None:
        plot_start_and_end_hours(self.db_path, days_range)

    def plot_task_time_distribution(self) -> None:
        plot_task_time_distribution(self.db_path)

    def plot_work_vs_break_time_distribution(self) -> None:
        plot_work_vs_break_time_distribution(self.db_path)

    def plot_daily_skipped_vs_completed_tasks(self, days_range: int = None) -> None:
        plot_daily_skipped_vs_completed_tasks(self.db_path, days_range)

    def plot_event_schedule(self, days_range: int = None) -> None:
        plot_event_schedule(self.db_path, days_range)
