from src.director import Director
from src.decorator import track_function
import time

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
def organize_desk():
    d.print("Organize your desk.\n\nMake sure everything is in its place.\n\n")
    d.input()


@track_function
def organize_digital_files():
    d.print("Organize your digital files.\n\n")
    d.print("Start by cleaning up your desktop.\n\n")
    d.input()
    d.print("Now, pick one specific folder and organize its contents.\n\n")
    d.input()
    d.print(
        "Open your email inbox and mark the spam messages by blocking the sender.\n\n"
    )
    d.input()


@track_function
def transcribe_highlighted_text():
    d.print("Pick a book already read and highlighted.\n\n")
    d.input()
    d.clear()
    d.print("Write down the title of the book in the new Google Docs document.\n\n")
    d.open_webpage("https://docs.google.com/document/u/0/create?usp=docs_home&ths=true")
    d.input()
    d.clear()
    d.print("Transcribe all the highlighted text.\n\n")
    d.input()
    d.clear()
    d.print("Read the text and correct it.\n\n")
    d.input()
    d.clear()
    d.print("Save the document as a PDF.\n\n")
    d.input()
    d.clear()
    d.print(
        "Store the PDF to your summaries folder within your organization system.\n\n"
    )
    d.input()


@track_function
def make_the_bed():
    d.print("Open the blinds.\n\n")
    d.input()
    d.clear()
    d.print("Make the bed.\n\n")
    d.input()


@track_function
def prepare_tomorrow_clothes():
    d.print("Pick a T-shirt and leave it on the shelf.\n\n")
    d.input()
    d.print("Pick a pair of pants and leave them on the shelf.\n\n")
    d.input()
    d.print("Pick a pair of socks and leave them on the shelf.\n\n")
    d.input()
    d.print("Pick up the underwear and put them on the shelf.\n\n")
    d.input()


@track_function
def clean_room():
    d.print("Put on some good music")
    d.input()
    d.print("Prepare the cleaning tools:\n\n\n")
    time.sleep(2)
    d.print("- A mop bucket with new water\n\n")
    time.sleep(1)
    d.print("- A small bucket with water, a little bit of bleach and one cloth\n\n")
    time.sleep(1)
    d.print("- Paper towels and glass window cleaner\n\n")
    time.sleep(1)
    d.print("- A bag for the trash\n\n")
    time.sleep(1)
    d.input()
    d.print("Put the desk things on the bed\n\n")
    d.input()
    d.print("Clean the window, the whiteboard and the mirror\n\n")
    d.input()
    d.print("Clean the desk\n\n")
    d.input()
    d.print("Put the desk things in the desk\n\n")
    d.input()
    d.print("Clean the furniture\n\n")
    d.input()
    d.print("Clean the floor\n\n")
    d.input()
    d.print("Take the trash out\n\n")
    d.input()


@track_function
def washing_machine():
    d.print("Do the laundry\n\n")
    d.print("Decide what to wash\n\n\n")
    time.sleep(2)
    d.print("- Clothes\n\n")
    time.sleep(1)
    d.print("- Towels\n\n")
    time.sleep(1)
    d.print("- Bed sheets\n\n")
    time.sleep(1)
    d.input()
    d.print("Put the clothes in the washing machine for 30 minutes\n\n")
    d.input()
    d.print("Set an alarm for 30 minutes from now\n\n")
    d.input()
    d.print("You can continue working with the rest of your tasks now.\n\n")
    d.print("When the alarm goes off, put the clothes in the dryer.\n\n")
    d.print("If you are busy when the alarm goes off, you may just take the clothes out of the washing machine and hang them to dry when you finish your task.")
    d.input()

