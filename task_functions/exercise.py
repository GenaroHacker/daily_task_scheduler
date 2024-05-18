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
#d.input()

@track_function
def go_to_gym():
    d.print("Put on your gym clothes and shoes.")
    d.input()
    d.print("Prepare a bottle of water with electrolytes and grab your gym card and a towel.")
    d.input()
    d.print("Go to the gym and complete your workout routine.")
    d.input()

@track_function
def do_40_pushups():
    d.print("Do 20 pushups.")
    d.input()
    d.print("Do 20 more pushups.")
    d.input()
