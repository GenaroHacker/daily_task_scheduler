import os
import json
import time


class DynamicTextPrinter:
    def __init__(
        self,
        max_line_length=80,
        char_delay=0.04,
        acceleration_factor=2.0,
        words_data_path="assets/data/top_1000_words.json",
    ):
        """Initialize the printer with configurable text output properties."""
        self.max_line_length = max_line_length
        self.char_delay = char_delay
        self.acceleration_factor = acceleration_factor
        self.common_words, self.speed_factors = self.load_common_words(words_data_path)

    def load_common_words(self, path):
        """Load the top 1000 words from a JSON file and compute speed factors based on their frequency."""
        with open(path, "r") as file:
            words = json.load(file)

        # Harmonic sum for the first 1000 ranks to normalize the speed factors
        harmonic_sum = sum(1 / i for i in range(1, 1001))
        base_factor = 1 / harmonic_sum  # Normalization factor for the least common word
        factor_range = (
            self.acceleration_factor - 1
        )  # Range between most and least common word's factors

        # Calculate speed factors for each word using linear interpolation
        factors = {
            word: 1 + factor_range * (1 - rank / 999) for rank, word in enumerate(words)
        }
        return words, factors

    def calculate_delay(self, word, is_newline=False):
        """Calculate the delay for a word based on its length and frequency, adjusted for punctuation and new lines."""
        if not word:
            return 0.5 if is_newline else 0.0  # Newline handling

        base_delay = self.char_delay * len(word)
        # Apply speed factor from precomputed values, defaulting to 1 for words not in the list
        speed_factor = self.speed_factors.get(word, 1)
        adjusted_delay = base_delay / speed_factor

        if word[-1] in ".,!?":
            adjusted_delay += 0.2  # Additional delay for punctuation
        if is_newline:
            adjusted_delay += 0.5  # Additional delay for new lines

        return adjusted_delay

    def print(self, text):
        """Print text with dynamic delays mimicking the principles of animation."""
        lines = text.split("\n")
        for line in lines:
            current_line_length = 0
            words = line.split()
            for index, word in enumerate(words):
                if current_line_length + len(word) + 1 > self.max_line_length:
                    print()  # Handle line breaks
                    current_line_length = 0

                for char in word:  # Print characters one at a time
                    print(char, end="", flush=True)
                    time.sleep(self.calculate_delay(word) / len(word))
                print(end=" ", flush=True)  # Add space after the word
                current_line_length += len(word) + 1

            print()  # Print newline if needed
            if lines[-1] != line:
                time.sleep(self.calculate_delay(""))  # Delay for new line handling
