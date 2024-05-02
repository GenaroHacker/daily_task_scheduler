from src.director_modules.projectdatabasemanager import ProjectDatabaseManager
from src.director_modules.scriptcommandexecutor import ScriptCommandExecutor
from src.director_modules.uihelper import UIHelper

class Director(ProjectDatabaseManager, ScriptCommandExecutor, UIHelper):
    def __init__(self):
        ProjectDatabaseManager.__init__(self)
        ScriptCommandExecutor.__init__(self)
        UIHelper.__init__(self)

    def manage_project(self, project_name, first_step):
        if self.start_new_project(project_name, first_step):
            print("Project management started.")
        else:
            print("Failed to start project management.")

    def deploy_project(self, script_name):
        print("Preparing to deploy project...")
        self.run_script(script_name)
        print("Deployment completed.")

    def monitor_progress(self, project):
        print("Monitoring progress for project:", project)
        self.make_progress(project)
