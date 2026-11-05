import sys
import time
from room1.introduction import typewriter_print, get_name, play_intro
from room1.safe import play_safe, safe_contents
from room1.computer import explore_computer, unlock_computer
from room1.body import dead_body
from project.state import print_hud
from . import state


# GLOBAL VARIABLES


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')  # Overwrite the line each second
        time.sleep(1)
        t -= 1

if __name__ == "__main__":
    # play intro
    get_name()
    play_intro()

    # game loop
    state.start=time.time()
    while True:
        # countdown(600)
        state.current_objective = 'Investigate the room'
        state.refresh_screen()
        typewriter_print('Investigate body (1)  Go to computer (2)  Go to the safe (3)', delay=0.03)
        choice = input()
        if choice =='1':
            state.current_objective = 'Investigate the body'
            dead_body()
        elif choice == '2':
            state.current_objective = 'Investigate the computer'
            if not state.computer_unlocked:
                state.computer_unlocked = unlock_computer()
            else:
                explore_computer()
        elif choice =='3':
            state.current_objective = 'Investigate the safe'
            if not state.safe_unlocked:
                state.safe_unlocked=play_safe()
            else:
                safe_contents()

#salfdjewqjfiwqjflwjlfjalfew
