from src.director_modules.metrics.time_worked import plot_time_worked

class Plotter:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def plot_time_worked(self, days: int) -> None:
        plot_time_worked(self.db_path, days)
