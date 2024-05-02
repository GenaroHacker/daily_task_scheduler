from src.director_modules.project_manager import ProjectDatabaseManager
from src.director_modules.code_executor import ScriptCommandExecutor
from src.director_modules.uihelper import UIHelper
import os

class Director(ProjectDatabaseManager, ScriptCommandExecutor, UIHelper):
    def __init__(self):
        ProjectDatabaseManager.__init__(self)
        ScriptCommandExecutor.__init__(self)
        UIHelper.__init__(self)

    def play_sound(self, sound="alarm.wav"):
        sound_path = os.path.join(self.SOUNDS_DIR, sound)
        self.execute_command(['aplay', sound_path])

    def open_webpage(self, url):
        self.execute_command(['xdg-open', url])