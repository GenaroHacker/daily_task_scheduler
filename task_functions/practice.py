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

@track_function
def solve_leetcode_problem():
    d.print("Time to solve a LeetCode problem.\n\n")
    time.sleep(0.5)
    d.print("Start by grabbing a pen and a clipboard.\n\n")
    d.input()
    d.clear()
    d.print("Choose a problem from the list of available problems.\n\n")
    time.sleep(0.5)
    d.print("You can also select today's Daily Coding Challenge or a random problem.\n\n")
    d.open_webpage("https://leetcode.com/problemset/")
    d.input()
    d.clear()
    d.print("Write down the problem statement on the paper.\n\n")
    d.input()
    d.clear()
    d.print("Write down the function signature.")
    d.input()
    d.clear()
    d.print("Do a first read of the problem statement and constraints to get a general sense of the problem.\n\n")
    d.input()
    d.clear()
    d.print("(Optional) Go to the Solutions section to read the most popular solutions.\n\n")
    time.sleep(0.5)
    d.print("It's okey to do so. We are here to learn efficient algorithms and data structures, not to reinvent the wheel.\n\n")
    time.sleep(0.5)
    d.print('Efficient management without effective leadership is, as one individual phrased it, "like straightening deck chairs on the Titanic."')
    d.input()
    d.clear()
    d.print("Time to start solving the problem on paper.\n\n")
    time.sleep(0.5)
    d.print("At this stage, you are still allowed to look at the Solutions but not the code written in the language you are using.\n\n")
    time.sleep(0.5)
    d.print("You can also search infroamtion on the internet or use other tools to help you solve the problem as long as you don't read code written in the language you are using.\n\n")
    time.sleep(0.5)
    d.print("Think about the properties of the class and the helper methods you will need.\n\n")
    time.sleep(0.5)
    d.print("Try to summarize the problem in your own words.\n\n")
    time.sleep(0.5)
    d.print("Ask questions to yourself...\n\n")
    time.sleep(0.5)
    d.print("-What are the inputs and outputs?\n\n")
    time.sleep(0.5)
    d.print("-Are you going to include unit tests?\n\n")
    time.sleep(0.5)
    d.print("-How are you going to name the properties and methods?\n\n")
    d.input()
    d.clear()
    d.print("Code the solution in the code editor.\n\n")
    time.sleep(0.5)
    d.print("Submit your solution to the LeetCode platform when you are ready.\n\n")
    time.sleep(0.5)
    d.print("Press enter once you have submitted the solution successfully.\n\n")
    d.open_webpage("https://colab.research.google.com/#create=true")
    d.input()
    d.clear()
    d.print("Congratulations! You have solved the problem.\n\n")
    time.sleep(0.5)
    d.print("If you have learned something new, like a new data structure or algorithm, write it down in your preferred reference storing system.\n\n")



@track_function
def list_gratitude_journal():
    d.print("Grab a pen and paper.\n\n")
    d.input()
    d.clear()
    d.print("Write down the title 'Thanks for...' and the date.\n\n")
    d.input()
    d.clear()
    for i in range(1, 11):
        d.print(f"List item {i}:")
        d.sleep(seconds=30)
        d.clear()
    d.print("Great job! You have completed your gratitude list.\n\n")
    time.sleep(0.5)
    d.print("You can store the list or discard it now.\n\n")
    time.sleep(0.5)
    d.input()
    d.clear()



@track_function
def practice_fast_typing():
    d.print("Open typing.com and practice the recommended lesson.\n\n")
    d.open_webpage("https://www.typing.com/student/lessons")
    d.input()

@track_function
def practice_calligraphy():
    d.print("Complete one page of the calligraphy practice notebook.\n\n")
    d.input()

@track_function
def take_exam():
    d.print("Open the skill_builder_exams main notebook, select the exam, and answer all the questions.\n\n")
    d.open_webpage("https://colab.research.google.com/github/GenaroHacker/skill_builder_exams/blob/main/main.ipynb")
    d.input()



@track_function
def implement_design_pattern():
    import random
    patterns = {
        "Creational": [
            {
                "name": "Abstract Factory",
                "definition": "Interface to create families of related or dependent objects without specifying their concrete classes",
                "aspects": "Families of product objects",
                "participants": "AbstractFactory, ConcreteFactory, AbstractProduct, ConcreteProduct"
            },
            {
                "name": "Builder",
                "definition": "Separate the construction of a complex object from its representation",
                "aspects": "How a composite object gets created",
                "participants": "Builder, ConcreteBuilder, Director, Product"
            },
            {
                "name": "Factory Method",
                "definition": "Define an interface for creating an object and let subclasses decide which class to instantiate",
                "aspects": "Subclass of object that is instantiated",
                "participants": "Creator, ConcreteCreator, Product, ConcreteProduct"
            },
            {
                "name": "Prototype",
                "definition": "Specify the kinds of objects to create using a prototypical instance",
                "aspects": "Class of object that is instantiated",
                "participants": "Prototype, ConcretePrototype"
            },
            {
                "name": "Singleton",
                "definition": "Ensure a class only has one instance",
                "aspects": "The single instance of a class",
                "participants": "Singleton"
            }
        ],
        "Structural": [
            {
                "name": "Adapter",
                "definition": "Convert the interface of a class into another interface clients expect",
                "aspects": "Interface to an object",
                "participants": "Target, Adapter, Adaptee"
            },
            {
                "name": "Bridge",
                "definition": "Decouple an abstraction from its implementation so they can vary independently",
                "aspects": "Implementation of an object",
                "participants": "Abstraction, RefinedAbstraction, Implementor, ConcreteImplementor"
            },
            {
                "name": "Composite",
                "definition": "Lets clients treat individual objects and compositions of objects uniformly",
                "aspects": "Structure and composition of an object",
                "participants": "Component, Leaf, Composite"
            },
            {
                "name": "Decorator",
                "definition": "Attach additional responsibilities to an object dynamically",
                "aspects": "Responsibilities of an object without subclassing",
                "participants": "Component, ConcreteComponent, Decorator, ConcreteDecorator"
            },
            {
                "name": "Facade",
                "definition": "Provide a unified interface to a set of interfaces in a subsystem",
                "aspects": "Interface to a subsystem",
                "participants": "Facade, Subsystem classes"
            },
            {
                "name": "Flyweight",
                "definition": "Use sharing to support large numbers of objects efficiently",
                "aspects": "Storage costs of objects",
                "participants": "Flyweight, ConcreteFlyweight, NonSharedConcreteFlyweight, FlyweightFactory"
            },
            {
                "name": "Proxy",
                "definition": "An object functioning as an interface to something else",
                "aspects": "How an object is accessed",
                "participants": "Subject, RealSubject, Proxy"
            }
        ],
        "Behavioral": [
            {
                "name": "Chain of Responsibility",
                "definition": "Command pass through processing objects until one handles it",
                "aspects": "Object that can process a request",
                "participants": "Handler, ConcreteHandler"
            },
            {
                "name": "Command",
                "definition": "Encapsulate a request as an object to perform an action or trigger an event at a later time",
                "aspects": "When and how a request is processed",
                "participants": "Command, ConcreteCommand, Invoker, Receiver"
            },
            {
                "name": "Interpreter",
                "definition": "Define a representation for the grammar of a given language along with an interpreter that uses the representation to interpret sentences in the language",
                "aspects": "Grammar and interpretation of a language",
                "participants": "AbstractExpression, TerminalExpression, NonterminalExpression, Context"
            },
            {
                "name": "Iterator",
                "definition": "Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation",
                "aspects": "How the elements of an aggregate are accessed",
                "participants": "Iterator, ConcreteIterator, Aggregate, ConcreteAggregate"
            },
            {
                "name": "Mediator",
                "definition": "Define an object that encapsulates how a set of objects interact",
                "aspects": "How and which objects interact with each other",
                "participants": "Mediator, ConcreteMediator, Colleague, ConcreteColleague"
            },
            {
                "name": "Memento",
                "definition": "Expose the private internal state of an object so it can be restored later",
                "aspects": "What private information is stored outside an object",
                "participants": "Memento, Originator, Caretaker"
            },
            {
                "name": "Observer",
                "definition": "The subject maintains a list of its observers and notifies them automatically when something changes by calling one of their methods",
                "aspects": "How the dependent objects stay up to date",
                "participants": "Subject, Observer, ConcreteSubject, ConcreteObserver"
            },
            {
                "name": "State",
                "definition": "Allow an object to alter its behavior when its internal state changes",
                "aspects": "States of an object",
                "participants": "Context, State, ConcreteState"
            },
            {
                "name": "Strategy",
                "definition": "Allow selecting an algorithm at runtime and which family of algorithms to use",
                "aspects": "An algorithm",
                "participants": "Strategy, ConcreteStrategy, Context"
            },
            {
                "name": "Template Method",
                "definition": "Method in an abstract class that defines the skeleton of an operation",
                "aspects": "Steps of an algorithm",
                "participants": "AbstractClass, ConcreteClass"
            },
            {
                "name": "Visitor",
                "definition": "Represent an operation to be performed on the elements of an object structure",
                "aspects": "Operations that can be applied to objects without changing their classes",
                "participants": "Visitor, ConcreteVisitor, Element, ConcreteElement, ObjectStructure"
            }
        ]
    }

    d.print("You are going to implement a design pattern.\n\n")
    time.sleep(0.5)
    d.print("Design patterns are reusable solutions to common problems in software design.\n\n")
    time.sleep(0.5)
    d.print("Start by grabbing pen and paper.")
    d.input()
    d.clear()

    creational_patterns = random.sample(patterns["Creational"], 3)
    structural_patterns = random.sample(patterns["Structural"], 3)
    behavioral_patterns = random.sample(patterns["Behavioral"], 3)

    d.print(f"Select a design pattern from the following list:\n\n"
            f"- Creational patterns:\n"
            f"  - {creational_patterns[0]['name']}\n"
            f"  - {creational_patterns[1]['name']}\n"
            f"  - {creational_patterns[2]['name']}\n\n"
            f"- Structural patterns:\n"
            f"  - {structural_patterns[0]['name']}\n"
            f"  - {structural_patterns[1]['name']}\n"
            f"  - {structural_patterns[2]['name']}\n\n"
            f"- Behavioral patterns:\n"
            f"  - {behavioral_patterns[0]['name']}\n"
            f"  - {behavioral_patterns[1]['name']}\n"
            f"  - {behavioral_patterns[2]['name']}\n")

    selected_pattern = input("Enter the name of the selected pattern: ")

    all_patterns = creational_patterns + structural_patterns + behavioral_patterns
    selected_info = next((pattern for pattern in all_patterns if pattern['name'] == selected_pattern), None)

    if selected_info:
        d.clear()
        d.print("Write down the name of the selected pattern along with the following information on the paper:\n\n\n")
        time.sleep(1)
        d.print("Selected pattern:\n")
        time.sleep(0.5)
        d.print(f"{selected_info['name']}\n\n")
        time.sleep(1)
        d.print("Definition:\n")
        time.sleep(0.5)
        d.print(f"{selected_info['definition']}\n\n")
        time.sleep(1)
        d.print("Aspect that can vary:\n")
        time.sleep(0.5)
        d.print(f"{selected_info['aspects']}\n\n")
        time.sleep(1)
        d.print("Participants:\n")
        time.sleep(0.5)
        d.print(f"{selected_info['participants']}\n\n")
        time.sleep(1)
    else:
        d.print("Selected pattern not found. Please make sure you enter the correct name.\n\n")
    d.input()
    d.clear()

    d.print("Grab the design pattern book and review the chapter of the selected pattern.\n\n")
    time.sleep(0.5)
    d.print("If you don't have the book, you can search for the pattern on the internet.\n\n")
    time.sleep(0.5)
    d.input()
    d.clear()

    d.print("Draw the UML diagrams of the general structure of the pattern on a piece of paper.\n\n")
    time.sleep(0.5)
    d.print("You don't need to draw the specific diagrams of the examples.\n\n")
    d.input()
    d.clear()

    d.print("Find a problem that can be solved with the selected pattern.\n\n")
    time.sleep(0.5)
    d.print("You can use the example from the book, find a problem on the internet, or imagine your own problem.\n\n")
    time.sleep(0.5)
    d.print("Write down the problem statement on the paper.\n\n")
    d.input()
    d.clear()

    d.print("Draw the diagram of classes. It represents the classes, their structure, and the static relationships between them.\n\n")
    time.sleep(0.5)
    d.print("A class is denoted by a rectangle with the class name in bold at the top.\n\n")
    time.sleep(0.5)
    d.print("The main methods of the class appear under the class name. The properties are shown below the methods.\n\n")
    time.sleep(0.5)
    d.print("If the font of a method appears in italics, it means that it is an abstract operation.\n\n")
    time.sleep(0.5)
    d.print("Class inheritance is represented by a triangle that connects a subclass to its parent class.\n\n")
    time.sleep(0.5)
    d.print("A reference to an object that represents an aggregation or part-whole relationship.\n\n")
    time.sleep(0.5)
    d.print("It is indicated by an arrow with a rhombus at its base.\n\n")
    time.sleep(0.5)
    d.print("An arrow without a rhombus denotes association.\n\n")
    time.sleep(0.5)
    d.print("To show which classes create instances of others we use an arrow with a dotted line.\n\n")
    time.sleep(0.5)
    d.print("We call this the 'Create' relationship. The arrow points to the class that is being instantiated.\n\n")
    time.sleep(0.5)
    d.print("A filled circle represents 'more than one.' When the circle appears at the end of a reference, it means that there are many objects referenced or added.\n\n")
    time.sleep(0.5)
    d.print("Finally, a rectangle with a bent corner includes pseudocode annotations allows to outline the implementations of the operations.\n\n")
    d.input()
    d.clear()

    d.print("Draw the diagram of objects. It shows a given object's structure in execution time.\n\n")
    time.sleep(0.5)
    d.print("An object diagram shows exclusively instances. Objects are named 'aSomething, where 'Something' is the class of the object.\n\n")
    time.sleep(0.5)
    d.print("The symbol of an object is a rectangle with rounded edges and a line that separates the name of the object from references to other objects.\n\n")
    time.sleep(0.5)
    d.print("The arrows indicate the referenced object.\n\n")
    d.input()
    d.clear()

    d.print("Draw the diagram of interactions. It shows the flow of messages between objects.\n\n")
    time.sleep(0.5)
    d.print("An interaction diagram shows the order in which requests between objects are executed.\n\n")
    time.sleep(0.5)
    d.print("In an interaction diagram, time flows from top to bottom.\n\n")
    time.sleep(0.5)
    d.print("A vertical line indicates the lifespan of a certain object.\n\n")
    time.sleep(0.5)
    d.print("The object naming convention is the same as that for object diagrams - ('aCar', 'anApple').\n\n")
    time.sleep(0.5)
    d.print("If no instance of the object is created until some time after the initial instant represented in the diagram, then its vertical line appears dotted until the moment of creation.\n\n")
    time.sleep(0.5)
    d.print("A vertical rectangle indicates that an object is active: that is, it is processing a request.\n\n")
    time.sleep(0.5)
    d.print("The operation can send requests to other objects: this is indicated by a horizontal arrow pointing to the receiving object. The name of the request is displayed above the arrow.\n\n")
    time.sleep(0.5)
    d.print("A request to create an object is indicated by a dotted arrow.\n\n")
    time.sleep(0.5)
    d.print("A request to the same sender object is represented with an arrow towards itself.\n\n")
    d.input()
    d.clear()

    d.print("Implement the design pattern.\n\n")
    d.open_webpage("https://colab.research.google.com/#create=true")
    d.input()
    d.clear()

    d.print("Copy the code to your preferred organization system in the practice/design_patterns folder.\n\n")
    d.input()
