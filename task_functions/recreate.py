from src.director import Director
from src.decorator import track_function
import time
from time import sleep

d = Director()
# d.clear()
# d.sleep(seconds=0.1)
# d.play_sound()
# d.run_script('example.sh')
# d.open_webpage("http://example.com")
# d.execute_command('ls')
# d.start_new_project('Sample Project', 'Initial Setup')
# d.make_progress('Sample Project')
# d.print("This is an example with a very long sentence...")
# d.input()


@track_function
def coffee():
    current_time = time.strftime("%H:%M:%S")
    if current_time < "07:00:00":
        d.print("Good morning!\n\n")
        sleep(1)
        d.print(f"It's {time.strftime('%H:%M:%S')}.\n\n")
        sleep(1)
        d.print("How about a cup of coffee?\n\n")
        d.input()
        d.clear()

        d.print("What makes you feel grateful today?:")
        input()
        d.input()
        d.clear()

        import json
        import random
        file_path = 'task_functions/func_modules/wake_up_phrases.json'
        with open(file_path, 'r') as file:
            data = json.load(file)
        phrases = data.get('wake_up_phrases', [])
        d.print(random.choice(phrases))

    else:
        d.print(
            f"It's {time.strftime('%H:%M:%S')}.\n\nYou should avoid drinking coffee now.\n\nIt's too late for that.\n\nContinue with the next task in your schedule instead.\n\n"
        )
    d.input()


@track_function
def breathing_exercise():
    d.print("Welcome to the breathing exercise!\n\n")
    sleep(1)
    d.print(
        "Stable, rhythmic breathing enhances RSA (Respiratory Sinus Arrhythmia), promoting cardiovascular efficiency and autonomic balance.\n\n"
    )
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
def plot_metrics():
    d.plot_time_worked()
    d.plot_event_schedule()
    d.plot_start_and_end_hours()
    d.plot_task_time_distribution()
    d.plot_work_vs_break_time_distribution()
    d.plot_daily_skipped_vs_completed_tasks()


@track_function
def eat():
    d.print("Time to eat!\n\n")
    sleep(0.5)
    d.print("Prepare a healthy meal and enjoy it.\n\n")
    d.input()


@track_function
def get_a_shower():
    d.print("Get a shower.\n\n")
    d.input()


@track_function
def shave_face():
    d.print("Shave face.\n\n")
    d.input()


@track_function
def brush_teeth():
    d.print("Brush teeth.\n\n")
    d.input()


@track_function
def take_supplements():
    d.print("Take supplements.\n\n")
    d.input()


@track_function
def drink_water():
    d.print("Drink one or two glasses of water.\n\n")
    d.input()


@track_function
def practice_meditation():
    d.print(
        "Sit down in a comfortable position, close your eyes, and press enter to start the meditation session.\n\n"
    )
    time.sleep(1)
    d.print(
        "Make sure your computer sound is not muted, since you will hear an alarm when the session is over.\n\n"
    )
    d.input()
    time.sleep(5)
    d.play_sound(sound="tibetan_gong.wav")
    d.clear()
    d.sleep(minutes=30)
    d.play_sound(sound="tibetan_gong.wav")
    time.sleep(3)
    d.clear()
    d.print("You have completed the meditation session.\n\n")
    time.sleep(1)
    d.print("Enjoy the rest of your day!\n\n")
    time.sleep(0.3)
    d.input()
