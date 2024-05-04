from src.director import Director
from src.scheduler import DailyTaskScheduler
from src.decorator import track_function
import time

if __name__ != '__main__':
    d = Director()
    #d.clear()
    #d.sleep(seconds=0.1)
    #d.play_sound()
    #d.run_script('example.sh')
    #d.open_webpage("http://example.com")
    #d.execute_command('ls')
    #d.start_new_project('Sample Project', 'Initial Setup')
    #d.make_progress('Sample Project')
    #d.print("Hello, world! This is an example with a very long sentence to test line breaking without cutting words short. Enjoy reading slowly.\nNew lines are properly handled with adaptive delay.")
    
    # Define functions
    @track_function
    def coffee():
        current_time = time.strftime("%H:%M:%S")
        if current_time < "07:00:00":
            d.print(f"Good morning!\n\nIt's {time.strftime('%H:%M:%S')}.\n\nHow about a cup of coffee?")
        elif current_time >= "07:00:00" and current_time < "10:30:00":
            d.print(f"It's {time.strftime('%H:%M:%S')}.\n\nYou are still in time for a cup of coffee if you want.\n\nContinue with the next task in your schedule once you're coffee is ready.\n\n")
        else:
            d.print(f"It's {time.strftime('%H:%M:%S')}.\n\nYou should avoid drinking coffee now.\n\nIt's too late for that.\n\nContinue with the next task in your schedule instead.\n\n")

    @track_function
    def organize_desk():
        d.print("Organize your desk.\n\nMake sure everything is in its place.\n\n")

    @track_function
    def organize_digital_files():
        d.print("Organize your digital files.\n\n")
        d.print("Start by cleaning up your desktop.\n\n")
        input()
        d.print("Now, pick one specific folder and organize its contents.\n\n")
        input()
        d.print("Open your email inbox and mark the spam messages by blocking the sender.\n\n")
        input()

    # Map functions to function keys
    functions = {
        'coffee': coffee,
        'desk': organize_desk,
        'files': organize_digital_files
    }

    # Define weekly schedule using function keys
    weekly_schedule = {
        0: ['coffee'],          # Monday
        1: ['coffee', 'desk'],  # Tuesday
        2: ['coffee', 'files'], # Wednesday
        3: ['coffee'],          # Thursday
        4: ['coffee', 'desk'],  # Friday
        5: ['coffee'],          # Saturday
        6: ['coffee']           # Sunday
    }

    scheduler = DailyTaskScheduler(weekly_schedule, functions)
    scheduler.execute_instructions()
