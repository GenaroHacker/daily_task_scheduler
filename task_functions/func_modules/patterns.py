from src.director import Director
import time
d = Director()



def implement_design_pattern():
    def open_diagram(image_path):
        import matplotlib.pyplot as plt
        import matplotlib.image as mpimg

        # Open an image file
        image = mpimg.imread(image_path)

        # Display the image
        plt.imshow(image)
        plt.axis("off")
        plt.show()

    import random

    patterns = {
        "Creational": [
            {
                "name": "Abstract factory",
                "definition": "Interface to create families of related or dependent objects without specifying their concrete classes",
                "aspects": "Families of product objects",
                "participants": "AbstractFactory, ConcreteFactory, AbstractProduct, ConcreteProduct",
            },
            {
                "name": "Builder",
                "definition": "Separate the construction of a complex object from its representation",
                "aspects": "How a composite object gets created",
                "participants": "Builder, ConcreteBuilder, Director, Product",
            },
            {
                "name": "Factory method",
                "definition": "Define an interface for creating an object and let subclasses decide which class to instantiate",
                "aspects": "Subclass of object that is instantiated",
                "participants": "Creator, ConcreteCreator, Product, ConcreteProduct",
            },
            {
                "name": "Prototype",
                "definition": "Specify the kinds of objects to create using a prototypical instance",
                "aspects": "Class of object that is instantiated",
                "participants": "Prototype, ConcretePrototype",
            },
            {
                "name": "Singleton",
                "definition": "Ensure a class only has one instance",
                "aspects": "The single instance of a class",
                "participants": "Singleton",
            },
        ],
        "Structural": [
            {
                "name": "Adapter",
                "definition": "Convert the interface of a class into another interface clients expect",
                "aspects": "Interface to an object",
                "participants": "Target, Adapter, Adaptee",
            },
            {
                "name": "Bridge",
                "definition": "Decouple an abstraction from its implementation so they can vary independently",
                "aspects": "Implementation of an object",
                "participants": "Abstraction, RefinedAbstraction, Implementor, ConcreteImplementor",
            },
            {
                "name": "Composite",
                "definition": "Lets clients treat individual objects and compositions of objects uniformly",
                "aspects": "Structure and composition of an object",
                "participants": "Component, Leaf, Composite",
            },
            {
                "name": "Decorator",
                "definition": "Attach additional responsibilities to an object dynamically",
                "aspects": "Responsibilities of an object without subclassing",
                "participants": "Component, ConcreteComponent, Decorator, ConcreteDecorator",
            },
            {
                "name": "Facade",
                "definition": "Provide a unified interface to a set of interfaces in a subsystem",
                "aspects": "Interface to a subsystem",
                "participants": "Facade, Subsystem classes",
            },
            {
                "name": "Flyweight",
                "definition": "Use sharing to support large numbers of objects efficiently",
                "aspects": "Storage costs of objects",
                "participants": "Flyweight, ConcreteFlyweight, NonSharedConcreteFlyweight, FlyweightFactory",
            },
            {
                "name": "Proxy",
                "definition": "An object functioning as an interface to something else",
                "aspects": "How an object is accessed",
                "participants": "Subject, RealSubject, Proxy",
            },
        ],
        "Behavioral": [
            {
                "name": "Chain of responsibility",
                "definition": "Command pass through processing objects until one handles it",
                "aspects": "Object that can process a request",
                "participants": "Handler, ConcreteHandler",
            },
            {
                "name": "Command",
                "definition": "Encapsulate a request as an object to perform an action or trigger an event at a later time",
                "aspects": "When and how a request is processed",
                "participants": "Command, ConcreteCommand, Invoker, Receiver",
            },
            {
                "name": "Interpreter",
                "definition": "Define a representation for the grammar of a given language along with an interpreter that uses the representation to interpret sentences in the language",
                "aspects": "Grammar and interpretation of a language",
                "participants": "AbstractExpression, TerminalExpression, NonterminalExpression, Context",
            },
            {
                "name": "Iterator",
                "definition": "Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation",
                "aspects": "How the elements of an aggregate are accessed",
                "participants": "Iterator, ConcreteIterator, Aggregate, ConcreteAggregate",
            },
            {
                "name": "Mediator",
                "definition": "Define an object that encapsulates how a set of objects interact",
                "aspects": "How and which objects interact with each other",
                "participants": "Mediator, ConcreteMediator, Colleague, ConcreteColleague",
            },
            {
                "name": "Memento",
                "definition": "Expose the private internal state of an object so it can be restored later",
                "aspects": "What private information is stored outside an object",
                "participants": "Memento, Originator, Caretaker",
            },
            {
                "name": "Observer",
                "definition": "The subject maintains a list of its observers and notifies them automatically when something changes by calling one of their methods",
                "aspects": "How the dependent objects stay up to date",
                "participants": "Subject, Observer, ConcreteSubject, ConcreteObserver",
            },
            {
                "name": "State",
                "definition": "Allow an object to alter its behavior when its internal state changes",
                "aspects": "States of an object",
                "participants": "Context, State, ConcreteState",
            },
            {
                "name": "Strategy",
                "definition": "Allow selecting an algorithm at runtime and which family of algorithms to use",
                "aspects": "An algorithm",
                "participants": "Strategy, ConcreteStrategy, Context",
            },
            {
                "name": "Template method",
                "definition": "Method in an abstract class that defines the skeleton of an operation",
                "aspects": "Steps of an algorithm",
                "participants": "AbstractClass, ConcreteClass",
            },
            {
                "name": "Visitor",
                "definition": "Represent an operation to be performed on the elements of an object structure",
                "aspects": "Operations that can be applied to objects without changing their classes",
                "participants": "Visitor, ConcreteVisitor, Element, ConcreteElement, ObjectStructure",
            },
        ],
    }

    d.print("You are going to implement a design pattern.\n\n")
    time.sleep(0.5)
    d.print(
        "Design patterns are reusable solutions to common problems in software design.\n\n"
    )
    time.sleep(0.5)
    d.print("Start by grabbing pen and paper.")
    d.input()
    d.clear()

    creational_patterns = random.sample(patterns["Creational"], 3)
    structural_patterns = random.sample(patterns["Structural"], 3)
    behavioral_patterns = random.sample(patterns["Behavioral"], 3)

    d.print(
        f"Select a design pattern from the following list:\n\n"
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
        f"  - {behavioral_patterns[2]['name']}\n"
    )

    selected_pattern = input("Enter the name of the selected pattern: ").capitalize()

    all_patterns = creational_patterns + structural_patterns + behavioral_patterns
    selected_info = next(
        (pattern for pattern in all_patterns if pattern["name"] == selected_pattern),
        None,
    )

    while selected_info is None:
        selected_pattern = input(
            "Invalid pattern name. Enter the name of the selected pattern: "
        ).capitalize()
        selected_info = next(
            (
                pattern
                for pattern in all_patterns
                if pattern["name"] == selected_pattern
            ),
            None,
        )

    d.clear()
    d.print(
        "Write down the name of the selected pattern along with the following information on the paper:\n\n\n"
    )
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

    d.input()
    d.clear()

    d.print(
        "Grab the design pattern book and review the chapter of the selected pattern.\n\n"
    )
    time.sleep(0.5)
    d.print(
        "If you don't have the book, you can search for the pattern on the internet.\n\n"
    )
    time.sleep(0.5)
    d.input()
    d.clear()

    d.print(
        "Draw the UML diagrams of the general structure of the pattern on a piece of paper.\n\n"
    )
    time.sleep(0.5)
    d.print("You don't need to draw the diagrams of the specific examples.\n\n")
    d.input()
    d.clear()

    d.print("Find a problem that can be solved with the selected pattern.\n\n")
    time.sleep(0.5)
    d.print(
        "You can use the example from the book, find a problem on the internet, or imagine your own problem.\n\n"
    )
    time.sleep(0.5)
    while True:  # problem must be at least 3 characters long
        problem = input("Enter the problem statement: ")
        if len(problem) >= 3:
            break
    d.clear()
    d.print("Write down the problem statement on your paper:\n\n\n")
    time.sleep(0.5)
    d.print(f"- {problem}\n\n")
    d.input()
    d.clear()

    # diagram of classes
    d.print(
        "Draw the diagram of classes. It represents the classes, their structure, and the static relationships between them.\n\n"
    )
    time.sleep(0.5)
    d.print("Think about the classes that will be part of your solution.\n\n")
    time.sleep(0.7)
    d.print(
        f"Consider both the general participants of the {selected_info['name']} pattern ({selected_info['participants']}) and how they will be implemented in your specific problem ({problem}).\n\n\n\n"
    )
    time.sleep(1.5)
    d.print("The diagram of classes follows the following conventions:\n\n\n")
    time.sleep(0.7)
    d.print(
        "A class is denoted by a rectangle with the class name in bold at the top.\n\n"
    )
    time.sleep(0.5)
    d.print(
        "The main methods of the class appear under the class name. The properties are shown below the methods.\n\n"
    )
    time.sleep(0.5)
    d.print(
        "If the font of a method appears in italics, it means that it is an abstract operation.\n\n"
    )
    time.sleep(0.5)
    d.print(
        "Class inheritance is represented by a triangle that connects a subclass to its parent class.\n\n"
    )
    time.sleep(0.5)
    d.print(
        "A reference to an object that represents an aggregation or part-whole relationship. It is indicated by an arrow with a rhombus at its base.\n\n"
    )
    time.sleep(0.5)
    d.print(
        "An arrow without a rhombus denotes association. If Class A points to Class B, it means Class A is using or talking to Class B.\n\n"
    )
    time.sleep(0.5)
    d.print(
        "To show which classes create instances of others we use an arrow with a dotted line. We call this the 'Create' relationship. The arrow points to the class that is being instantiated.\n\n"
    )
    time.sleep(0.5)
    d.print(
        "A filled circle represents 'more than one.' When the circle appears at the end of a reference, it means that there are many objects referenced or added.\n\n"
    )
    time.sleep(0.5)
    d.print(
        "Finally, a rectangle with a bent corner includes pseudocode annotations allows to outline the implementations of the operations.\n\n"
    )
    time.sleep(2)
    open_diagram("assets/images/class.png")
    d.input()
    d.clear()

    # diagram of objects
    d.print(
        "Draw the diagram of objects. It shows a given object's structure in execution time.\n\n"
    )
    time.sleep(0.5)
    d.print(
        "An object diagram shows exclusively instances. Objects are named 'aSomething, where 'Something' is the class of the object.\n\n"
    )
    time.sleep(0.5)
    d.print(
        "The symbol of an object is a rectangle with rounded edges and a line that separates the name of the object from references to other objects.\n\n"
    )
    time.sleep(0.5)
    d.print("The arrows indicate the referenced object.\n\n")
    time.sleep(2)
    open_diagram("assets/images/object.png")
    d.input()
    d.clear()

    # diagram of interactions
    d.print(
        "Draw the diagram of interactions. It shows the flow of messages between objects.\n\n"
    )
    time.sleep(0.5)
    d.print(
        "An interaction diagram shows the order in which requests between objects are executed.\n\n"
    )
    time.sleep(0.5)
    d.print("In an interaction diagram, time flows from top to bottom.\n\n")
    time.sleep(0.5)
    d.print("A vertical line indicates the lifespan of a certain object.\n\n")
    time.sleep(0.5)
    d.print(
        "The object naming convention is the same as that for object diagrams - ('aCar', 'anApple').\n\n"
    )
    time.sleep(0.5)
    d.print(
        "If no instance of the object is created until some time after the initial instant represented in the diagram, then its vertical line appears dotted until the moment of creation.\n\n"
    )
    time.sleep(0.5)
    d.print(
        "A vertical rectangle indicates that an object is active: that is, it is processing a request.\n\n"
    )
    time.sleep(0.5)
    d.print(
        "The operation can send requests to other objects: this is indicated by a horizontal arrow pointing to the receiving object. The name of the request is displayed above the arrow.\n\n"
    )
    time.sleep(0.5)
    d.print("A request to create an object is indicated by a dotted arrow.\n\n")
    time.sleep(0.5)
    d.print(
        "A request to the same sender object is represented with an arrow towards itself.\n\n"
    )
    time.sleep(2)
    open_diagram("assets/images/interaction.png")
    d.input()
    d.clear()

    d.print("Implement the design pattern.\n\n")
    d.open_webpage("https://colab.research.google.com/#create=true")
    d.input()
    d.clear()

    d.print(
        "Copy the code to your preferred organization system in the practice/design_patterns folder.\n\n"
    )
    d.input()

    d.print("Congratulations! You have successfully implemented a design pattern.\n\n")

