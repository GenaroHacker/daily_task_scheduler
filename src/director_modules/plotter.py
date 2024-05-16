from src.director_modules.metrics.time_worked import plot_time_worked
from src.director_modules.metrics.worked_hours import plot_start_and_end_hours

class Plotter:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def plot_time_worked(self, days: int) -> None:
        plot_time_worked(self.db_path, days)

    def plot_start_and_end_hours(self, days_range: int = None) -> None:
        plot_start_and_end_hours(self.db_path, days_range)