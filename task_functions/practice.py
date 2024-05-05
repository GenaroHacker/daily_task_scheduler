from src.director import Director
from src.decorator import track_function

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



@track_function
def pomodoro_session():
    d.print("You are going to start a Pomodoro session.\n\n")
    time.sleep(0.5)
    d.print("The total time expected to complete is two and a half hours.\n\n")
    time.sleep(0.5)
    d.print("Grab your study materials and a highlighter.\n\nThen, press enter to start the first focus block.\n\n")
    input()

    # Define the schedule of focus blocks and breaks
    sessions = [
        ("focus", "first", 25),
        ("break", "short", 5),
        ("focus", "second", 25),
        ("break", "short", 5),
        ("focus", "third", 25),
        ("break", "short", 5),
        ("focus", "fourth", 25),
        ("break", "long", 10),
        ("focus", "last", 25)
    ]

    def handle_session(session_type, description, duration):
        if session_type == "focus":
            d.print(f"The {description} focus block starts now.\n\n")
        else:
            d.print(f"Take a {description} break for {duration} minutes.\n\n")
        
        d.play_sound(sound="beeps.wav" if session_type == "focus" else "chimes.wav")
        d.sleep(minutes=duration)
        d.play_sound(sound="alarm.wav")
        d.print(f"The {description} {'focus block' if session_type == 'focus' else 'break'} is over.\n\n")
        time.sleep(0.5)

    # Execute each session according to the defined schedule
    for session_type, description, duration in sessions:
        handle_session(session_type, description, duration)

    d.print("Congratulations! You have completed a full Pomodoro session.\n\n")
    d.print("Press enter to continue with the next task in your schedule.\n\n")
    input()