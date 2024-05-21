from src.director import Director
from src.decorator import track_function
from task_functions.func_modules.gtd import GettingThingsDone

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
def get_things_done(db_path="assets/data/smark.db"):
    gtd = GettingThingsDone(db_path)
    gtd.run()


@track_function
def make_progress():
    d.make_progress()


@track_function
def rank_projects():
    d.rank_projects()


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
