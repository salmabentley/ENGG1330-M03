import sys
import time
from termcolor import colored
import os
from room1.md import display_md


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

start=0
timer=0
paused_time=0
energy=100
energy_decrease=0.5
photo_found=False
money_found=False
name=''

def typewriter_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 
    time.sleep(1)

def time_left():
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
    sys.stdout.write(colored('Help (H) Pause (Q) + Enter'.center(80),'red',attrs=['reverse'])+'\n')
    sys.stdout.write(colored(f'{hud_left}{' ' * max(0, space_padding)}{hud_right}\n','red', 'on_white', attrs=['reverse']))
    sys.stdout.write("═" * 80 + "\n")

def refresh_screen():
    print("\033[H\033[J", end="")
    print_hud(current_objective)

def pause_game():
    global paused_time, start

    refresh_screen()
    print("\n" + "="*30)
    print("PAUSED".center(30))
    print("="*30)
    print("1. Resume Game")
    print("2. Restart Game")
    print("3. Quit to Desktop")
    
    # Record when the pause started
    pause_start = time.time()
    
    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            # Accumulate the time spent in the pause menu
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
    elif ans.strip().lower() == 'q':
            pause_game()