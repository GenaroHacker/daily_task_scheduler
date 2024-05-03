import time
import random
import math

class DynamicTextPrinter:
    def __init__(self, max_line_length=80):
        """ Initialize the printer with configurable text output properties. """
        self.max_line_length = max_line_length
        self.last_deviation = 1.0  # Starting point with no deviation

    def _text_strategy(self, element: str, index: int, is_newline: bool) -> float:
        """ Internal strategy to calculate delay based on the animation principles. """
        if not element:  # Check if element is empty
            return 0.5 if is_newline else 0.0  # Apply delay for newlines
        base_delay = 0.1 * len(element)
        if element[-1] in ".,!?":
            base_delay += 0.2  # Slow in for punctuation
        if is_newline:
            base_delay += 0.5  # Anticipation for new lines
        return base_delay

    def _deviate(self, base_delay: float) -> float:
        """ Apply deviation logic to simulate 'Follow Through' and 'Overlapping Action'. """
        deviation = random.uniform(-0.5, 0.5)
        new_deviation = self.last_deviation * math.exp(deviation * 0.2)  # Adding exponential decay
        new_deviation = max(0.5, min(1.5, math.fabs(new_deviation)))  # Ensuring deviation stays reasonable
        self.last_deviation = new_deviation
        return base_delay * new_deviation

    def print(self, text: str, speed_scale: float = 1.0):
        """ Print text with dynamic delays mimicking the principles of animation. """
        lines = text.split('\n')
        for line in lines:
            current_line_length = 0
            words = line.split()
            for index, word in enumerate(words):
                if current_line_length + len(word) > self.max_line_length:
                    print()  # Implement 'Staging' by handling line breaks
                    current_line_length = 0
                print(word, end=' ', flush=True)
                delay = self._deviate(self._text_strategy(word, index, False) * speed_scale)
                time.sleep(delay)  # Apply 'Timing' to regulate the speed of text appearance
                current_line_length += len(word) + 1
            print()  # New line with anticipation and follow-through
            if lines[-1] != line:
                time.sleep(self._deviate(self._text_strategy('', 0, True) * speed_scale))

