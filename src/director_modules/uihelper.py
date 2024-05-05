import sys
import time
import os

class UIHelper:
    SOUNDS_DIR = os.path.join('assets', 'sounds')

    def sleep(self, minutes=0, seconds=0):
        total_seconds = minutes * 60 + seconds
        interval = total_seconds / 40
        for i in range(1, 41):
            time.sleep(interval)
            progress = '#' * i
            remaining = '-' * (40 - i)
            sys.stdout.write('\r[{}]'.format(progress + remaining))
            sys.stdout.flush()
        print()

    def clear(self):
        os.system('clear')

    def play_sound(self, sound="alarm.wav"):
        sound_path = os.path.join(self.SOUNDS_DIR, sound)
        self.execute_command(['aplay', sound_path])

    def open_webpage(self, url):
        self.execute_command(['xdg-open', url])

    def input(self, prompt=''):
        print(f'\033[33m{prompt}\033[0m')
        print('\033[33mPress Enter to continue...\033[0m')
        return input()
