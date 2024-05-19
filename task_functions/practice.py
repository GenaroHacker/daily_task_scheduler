from src.director import Director
from src.decorator import track_function
import time

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
def pomodoro_session():
    d.print("You are going to start a Pomodoro session.\n\n")
    time.sleep(0.5)
    d.print("The total time expected to complete is two and a half hours.\n\n")
    time.sleep(0.5)
    d.print("Grab your study materials and a highlighter.\n\n")
    d.input()

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
    d.input()

@track_function
def guitar_loop_note():
    from random import choice
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    bpms = ["30", "40", "50"]

    note = choice(notes)
    bpm = choice(bpms)

    d.print("You are going to practice looping a note on the guitar.\n\n")
    time.sleep(0.5)
    d.print("Grab your guitar and a pick.\n\n")
    time.sleep(0.5)
    d.print("Tune the guitar.")
    d.input()
    d.clear()
    d.print(f"Set the metronome to 5/4 time signature and {bpm} bpm.\n\n")
    d.open_webpage("https://theonlinemetronome.com/online-metronome")
    d.input()
    d.clear()
    d.print(f"The note you will practice is {note} and the metronome is set to {bpm} bpm.\n\n")
    time.sleep(0.5)
    d.print("The exercise consists of looping the note in each string from the fret 0 to the fret 11.\n\n")
    time.sleep(0.5)
    d.print("You will start from the 1st string until you reach the 6th string.\n\n")
    time.sleep(0.5)
    d.print("If you make a mistake, wait for the next loop to start again from the correct beat.\n\n")
    time.sleep(0.5)
    d.print("Use only the index finger to press the strings.\n\n")
    time.sleep(0.5)
    d.print("When you are ready, start the metronome and begin the exercise.\n\n")
    time.sleep(0.5)
    d.print("The pick goes up for strings 2, 4, and 6, and down for strings 1, 3, and 5.\n\n")
    time.sleep(0.5)
    d.print("You must complete 3 loops in a row.\n\n")
    d.input()


