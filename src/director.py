from src.director_modules.project_manager import ProjectDatabaseManager
from src.director_modules.code_executor import ScriptCommandExecutor
from src.director_modules.uihelper import UIHelper
from src.director_modules.printer import DynamicTextPrinter
from src.director_modules.plotter import Plotter

class Director(ProjectDatabaseManager, ScriptCommandExecutor, UIHelper, DynamicTextPrinter, Plotter):
    def __init__(self, events=None, days_range=30):
        ProjectDatabaseManager.__init__(self)
        ScriptCommandExecutor.__init__(self)
        UIHelper.__init__(self)
        DynamicTextPrinter.__init__(self)
        Plotter.__init__(self, self.db_path)
        
