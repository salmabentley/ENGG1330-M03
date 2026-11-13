import sys
import time
from termcolor import colored
import os
from room1.md import display_md
import textwrap


# GLOBAL VARIABLES
safe_unlocked=False         #flag to store whether safe has been unlocked
computer_unlocked=False

current_objective = ''
current_room=1

body_investigated=False
computer_investigated = False
safe_investigated = False

#people that have been interacted with
peter=False
eleanor=False
george=False
gabrielle=False

eleanor_disabled=False
gabrielle_disabled=False

eleanor_food=False

start=0
timer=0
paused_time=0
energy=100
energy_decrease=0.5
photo_found=False
money_found=False
name=''
elapsed=0

import os
import sys
import time

def check_terminal_size():
    """
    Checks if the terminal is at least 80x24. 
    If smaller, pauses the game and displays a blocking resize message.
    """
    while True:
        try:
            # Get current terminal columns and rows
            size = os.get_terminal_size()
            cols = size.columns
            rows = size.lines
        except (AttributeError, OSError):
            # Fallback if running in a non-interactive environment where size can't be fetched
            return

        if cols >= 80 and rows >= 24:
            break  # Size is good, exit check loop

        # Clear screen and display warning that fits inside whatever small space they have
        sys.stdout.write("\033[H\033[J")
        warning_lines = [
            "!" * min(cols, 80),
            " TERMINAL TOO SMALL! ".center(cols, "!"),
            f" Current: {cols}x{rows} ".center(cols, " "),
            " Required: At least 80x24 ".center(cols, " "),
            " Please resize your terminal window. ".center(cols, " "),
            "!" * min(cols, 80)
        ]
        
        for line in warning_lines:
            print(line[:cols])
            
        # Check again after a brief pause so it auto-resumes the moment they expand the window
        time.sleep(0.5)

def typewriter_print(text, delay=0.03):
    wrapped_lines = textwrap.wrap(text, width=80)
    
    for line in wrapped_lines:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()  # Move to the next line when the wrapped line finishes
        
    time.sleep(1)

def time_left():
    global elapsed
    elapsed=time.time()-start-paused_time
    remaining=600-elapsed
    mins, secs = divmod(int(remaining), 60)
    string = '{:02d}:{:02d}'.format(mins, secs)
    return string

def print_hud(objective):
    """Draws the sticky header at the very top without breaking your existing code."""
    timer=time_left()
    sys.stdout.write("\033[H") # Jump cursor to top
    hud_left = f" OBJECTIVE: {objective}"
    if current_room==1:
        hud_right = f"TIME: {timer} "
    else:
        hud_right= f"ENERGY: {energy} "
    space_padding = 80 - (len(hud_left) + len(hud_right))
    #print header with reverse highlight & red text
    if current_room==1:
        sys.stdout.write(colored('Help (H) Pause (Q) + Enter'.center(80),'red',attrs=['reverse'])+'\n')
    else:
        sys.stdout.write(colored('Help (H) Pause (Q)'.center(80),'red',attrs=['reverse'])+'\n')
    sys.stdout.write(colored(f'{hud_left}{' ' * max(0, space_padding)}{hud_right}\n','red', 'on_white', attrs=['reverse']))
    sys.stdout.write("═" * 80 + "\n")

def refresh_screen():
    check_terminal_size()
    print("\033[H\033[J", end="")
    print_hud(current_objective)

def pause_game():
    global paused_time, start

    refresh_screen()
    print("\n" + "="*80)
    print("PAUSED".center(80))
    print("="*80)
    print("1. Resume Game".center(80))
    print("2. Restart Game".center(80))
    print("3. Quit to Desktop".center(80))
    
    # Record when the pause started
    pause_start = time.time()
    
    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            # Accumulate the time spent in the pause menu
            if current_room==1:
                paused_duration = time.time() - pause_start
                paused_time += paused_duration
            
            print("\nResuming game...\n")
            return 'resume'
            
        elif choice == '2':
            print("\nRestarting game...")
# This completely replaces the current python process with a fresh run of main.py
            os.execv(sys.executable, [sys.executable] + sys.argv)
            
        elif choice == '3':
            print("\nExiting game. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def check_player_input(ans):
    # checks if player pressed h or q
    if ans.strip().lower() == 'h':
            display_md('documents/help.md')
            refresh_screen()
    elif ans.strip().lower() == 'q':
            pause_game()
            refresh_screen()