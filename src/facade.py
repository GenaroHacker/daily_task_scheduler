from src.facade_modules.scheduler import DailyTaskScheduler

class Facade(DailyTaskScheduler):
    def __init__(self, schedule, functions):
        super().__init__(schedule, functions)
