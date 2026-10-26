import sys
import time
from introduction import typewriter_print, get_name, play_intro
from safe import play_safe, safe_contents

# GLOBAL VARIABLES
safe_unlocked=False

if __name__ == "__main__":
    get_name()
    play_intro()
    while True:
        typewriter_print('Investigate body (1)  Go to computer (2)  Go to the safe (3)', delay=0.03)
        choice = input()
        if choice =='3':
            if not safe_unlocked:
                safe_unlocked=play_safe()
            safe_contents()

#salfdjewqjfiwqjflwjlfjalfew
