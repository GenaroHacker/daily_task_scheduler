import subprocess
import os

class ScriptCommandExecutor:
    SCRIPTS_DIR = os.path.join('assets', 'scripts')

    def execute_command(self, command, shell=False):
        try:
            subprocess.run(command, shell=shell, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Command failed: {e}")

    def run_script(self, script_name):
        script_path = os.path.join(self.SCRIPTS_DIR, script_name)
        if script_name.endswith('.sh'):
            self.execute_command(f"bash {script_path}", shell=True)
        elif script_name.endswith('.py'):
            self.execute_command(f"python3 {script_path}", shell=True)
        else:
            raise ValueError("Unsupported script extension")
