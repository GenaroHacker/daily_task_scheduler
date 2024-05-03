from src.director import Director
from src.scheduler import DailyTaskScheduler
from src.decorator import track_function

if __name__ == '__main__':
    director = Director()
    director.clear()
    director.sleep(seconds=0.1)
    director.play_sound()
    director.run_script('example.sh')
    director.open_webpage("http://example.com")
    director.execute_command('ls')
    director.start_new_project('Sample Project', 'Initial Setup')
    director.make_progress('Sample Project')
    director.print("Hello, world! This is an example with a very long sentence to test line breaking without cutting words short. Enjoy reading slowly.\nNew lines are properly handled with adaptive delay.")
    
    # Define functions
    @track_function
    def function_A():
        print("Executing function A")

    @track_function
    def function_B():
        print("Executing function B")

    @track_function
    def function_C():
        print("Executing function C")

    @track_function
    def function_D():
        print("Executing function D")

    @track_function
    def function_E():
        print("Executing function E")

    # Map functions to function keys
    functions = {
        'A': function_A,
        'B': function_B,
        'C': function_C,
        'D': function_D,
        'E': function_E
    }

    # Define weekly schedule using function keys
    weekly_schedule = {
        0: ['A', 'B'],  # Monday
        1: ['C'],       # Tuesday
        2: ['A', 'C'],  # Wednesday
        3: ['D', 'E'],  # Thursday
        4: ['B', 'E'],  # Friday
        5: ['A'],       # Saturday
        6: ['E']        # Sunday
    }

    scheduler = DailyTaskScheduler(weekly_schedule, functions)
    scheduler.execute_instructions()
