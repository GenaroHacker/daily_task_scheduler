from src.director import Director
from src.decorator import track_function
import time
from time import sleep

d = Director()
#d.clear()
#d.sleep(seconds=0.1)
#d.play_sound()
#d.run_script('example.sh')
#d.open_webpage("http://example.com")
#d.execute_command('ls')
#d.start_new_project('Sample Project', 'Initial Setup')
#d.make_progress('Sample Project')
#d.print("This is an example with a very long sentence...")
#d.input()

@track_function
def coffee():
    current_time = time.strftime("%H:%M:%S")
    if current_time < "07:00:00":
        d.print(f"Good morning!\n\nIt's {time.strftime('%H:%M:%S')}.\n\nHow about a cup of coffee?")
    elif current_time >= "07:00:00" and current_time < "10:30:00":
        d.print(f"It's {time.strftime('%H:%M:%S')}.\n\nYou are still in time for a cup of coffee if you want.\n\nContinue with the next task in your schedule once you're coffee is ready.\n\n")
    else:
        d.print(f"It's {time.strftime('%H:%M:%S')}.\n\nYou should avoid drinking coffee now.\n\nIt's too late for that.\n\nContinue with the next task in your schedule instead.\n\n")
    d.input()

@track_function
def breathing_exercise():
    d.print("Welcome to the breathing exercise!\n\n")
    sleep(1)
    d.print("Stable, rhythmic breathing enhances RSA (Respiratory Sinus Arrhythmia), promoting cardiovascular efficiency and autonomic balance.\n\n")
    sleep(2)
    d.print("Sit straight on your chair, with your feet flat on the floor.\n\n")
    sleep(2)
    d.print("Make sure your lower back is supporting your upper body.\n\n")
    sleep(2)
    d.print("Keep your chest still and let your diaphragm do the work.\n\n")
    sleep(1)
    d.print("Press enter when you are ready to start.\n")
    sleep(0.3)
    d.input()
    d.clear()
    sleep(1)

    for i in range(40):
        d.print("Inhale")
        d.sleep(seconds=3)
        d.print("Hold")
        d.sleep(seconds=1)
        d.print("Exhale")
        d.sleep(seconds=6)
        d.print("Wait")
        d.sleep(seconds=2)
        d.clear()

    d.clear()
    d.print("You have completed the breathing exercise.\n\n")
    sleep(1)
    d.print("Enjoy the rest of your day!\n")
    sleep(0.3)
    d.input()

@track_function
def plot_work_time_percentage():
    d.plot_time_worked()
    d.plot_start_and_end_hours()
    d.plot_task_time_distribution()
