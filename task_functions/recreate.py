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
def coffee():
    current_time = time.strftime("%H:%M:%S")
    if current_time < "07:00:00":
        d.print(f"Good morning!\n\nIt's {time.strftime('%H:%M:%S')}.\n\nHow about a cup of coffee?")
    elif current_time >= "07:00:00" and current_time < "10:30:00":
        d.print(f"It's {time.strftime('%H:%M:%S')}.\n\nYou are still in time for a cup of coffee if you want.\n\nContinue with the next task in your schedule once you're coffee is ready.\n\n")
    else:
        d.print(f"It's {time.strftime('%H:%M:%S')}.\n\nYou should avoid drinking coffee now.\n\nIt's too late for that.\n\nContinue with the next task in your schedule instead.\n\n")
    d.input()
