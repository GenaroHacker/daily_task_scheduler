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
#d.input(prompt='')

@track_function
def organize_desk():
    d.print("Organize your desk.\n\nMake sure everything is in its place.\n\n")


@track_function
def organize_digital_files():
    d.print("Organize your digital files.\n\n")
    d.print("Start by cleaning up your desktop.\n\n")
    d.input()
    d.print("Now, pick one specific folder and organize its contents.\n\n")
    d.input()
    d.print("Open your email inbox and mark the spam messages by blocking the sender.\n\n")
    d.input()
