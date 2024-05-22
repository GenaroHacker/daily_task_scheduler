import sqlite3
import os
class IdeaManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.initialize_database()

    def initialize_database(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS ideas (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name TEXT NOT NULL
            )"""
        )
        conn.commit()
        conn.close()

    def get_last_idea(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM ideas ORDER BY id DESC LIMIT 1")
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None

    def add_idea(self, idea):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ideas (name) VALUES (?)", (idea,))
        conn.commit()
        conn.close()

    def get_best_item(self, items):
        def compare_items(item1, item2):
            while True:
                print(f" [ 1 ] [{item1}] ?")
                print(f" [ 2 ] [{item2}] ?")
                choice = input(" --> ? ")
                if choice == '1':
                    return item1
                elif choice == '2':
                    return item2
                else:
                    print("Invalid input. Please type 1 or 2.")

        best_item = items[0]
        for i in range(1, len(items)):
            best_item = compare_items(best_item, items[i])
        return best_item

    def run(self):
        last_idea = self.get_last_idea()
        if last_idea:
            pass
        else:
            print("No ideas found. Please enter 5 new ideas.")

        new_ideas = []
        for i in range(5):
            print("Provide 5 new ideas inspired by the following:\n\n")
            print(f'"{last_idea}"\n\n')
            new_idea = input(f"Idea {i + 1}: ")
            new_ideas.append(new_idea)
            os.system("clear")

        best_idea = self.get_best_item(new_ideas)
        print(f"Best idea selected: {best_idea}")
        self.add_idea(best_idea)

if __name__ == "__main__":
    db_path = "ideas.db"
    manager = IdeaManager(db_path)
    manager.run()
