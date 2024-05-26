import time
import json
import random
from typing import List

class Coffee:
    def __init__(self, d, file_path: str = 'task_functions/func_modules/wake_up_phrases.json'):
        self.d = d
        self.file_path = file_path

    def _get_current_time(self) -> str:
        return time.strftime("%H:%M:%S")

    def _load_phrases(self) -> List[str]:
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return data.get('wake_up_phrases', [])

    def _get_random_phrase(self, phrases: List[str]) -> str:
        return random.choice(phrases)

    def _get_random_question(self, questions: List[str]) -> str:
        return random.choice(questions)

    def _morning_routine(self):
        self.d.print("Good morning!\n\n")
        time.sleep(1)
        self.d.print(f"It's {self._get_current_time()}.\n\n")
        time.sleep(1)
        self.d.print("How about a cup of coffee?\n\n")
        self.d.input()
        self.d.clear()

        self.d.print("What makes you feel grateful today?:")
        input()
        self.d.input()
        self.d.clear()

        questions = [
            "Who exemplifies this in your life?",
            "How would you measure your progress in integrating this into your life?",
            "How would you expand the idea?",
            "How can you apply this today?",
            "How can you simplify this?",
            "What’s the simplest approach?",
            "How does this benefit others?",
            "What’s the core message here?"
        ]

        phrases = self._load_phrases()
        selected_phrase = self._get_random_phrase(phrases)
        selected_question = self._get_random_question(questions)

        self.d.print("Give yourself a moment to think about the following...\n\n")
        time.sleep(1)
        self.d.print(selected_question)
        time.sleep(2)
        self.d.print(selected_phrase)
        time.sleep(4)
        self.d.clear()

        print(selected_question)
        print(selected_phrase)
        time.sleep(2)
        self.d.sleep(seconds=60)
        input(" ?: ")
        time.sleep(1)

    def _evening_routine(self):
        self.d.print(
            f"It's {self._get_current_time()}.\n\nYou should avoid drinking coffee now.\n\nIt's too late for that.\n\nContinue with the next task in your schedule instead.\n\n"
        )
        self.d.input()

    def execute(self):
        current_time = self._get_current_time()
        if current_time < "07:00:00":
            self._morning_routine()
        else:
            self._evening_routine()
