import sys
import time
from termcolor import colored
import os
from room1.md import display_md
import textwrap


# GLOBAL VARIABLES [ROOM 1]
safe_unlocked=False             #flag to store whether safe has been unlocked
computer_unlocked=False         #flag to store whether the computer has been unlocked

current_objective = ''          #track current objective
current_room=1                  #tracks the current room the player is in

body_investigated=False         #tracks whether the body has been interacted with yet
computer_investigated = False   #tracks whether the computer has been interacted with yet
safe_investigated = False       #tracks whether the safe has been interacted with yet

#people that have been interacted with
peter=False
eleanor=False
george=False
gabrielle=False

#GLOBAL VARIABLES [ROOM 2]

#flags that determine if certain npcs have been disabled due to poor dialogue choices in room 2
eleanor_disabled=False
gabrielle_disabled=False

eleanor_food=False  #checks whether player has interacted with George Tam about Eleanor giving him food. Triggers hidden dialogue with Eleanor Lan
photo_found=False   #flag for whether the photo has been found with Peter Lang in room 1. Triggers hidden dialogue with Peter Lang
money_found=False   #flag for whether money has been found in the safe in room 1. Triggers hidden dialogue with Eleanor Lan

# time variables
start=time.time()   #start time in seconds
timer=0             #formatted time string
paused_time=0       #time spent in pause menu
elapsed=0           #elapsed time in room 1

# energy variables
energy=100          #tracks player energy in room 2
energy_decrease=0.25 #rate at which energy decreases per step in room 2

name=''             #tracks player name

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

# types given text in a typewriter style with a delay between each character
def typewriter_print(text, delay=0.03):
    # wraps lines using text wrap to fit width limit
    wrapped_lines = textwrap.wrap(text, width=80)

    # prints each character in each line plus delay
    for line in wrapped_lines:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
        
    time.sleep(1)

# calculates time left in room 1
def time_left():
    global elapsed
    #subtracts paused time and start time from current time to get time elapsed in seconds
    elapsed=time.time()-start-paused_time

    #calculates remaining time in seconds
    remaining=600-elapsed

    #converts remaining time in seconds into minutes and seconds remaining to be displayed
    mins, secs = divmod(int(remaining), 60)

    #adds time to formatable string
    string = '{:02d}:{:02d}'.format(mins, secs)
    return string

#Draws the sticky header at the very top
def print_hud(objective):
    timer=time_left()
    sys.stdout.write("\033[H") # Jump cursor to top
    hud_left = f" OBJECTIVE: {objective}"

    #put timer on the hud if in room 1, else put the energy remaining
    if current_room==1:
        hud_right = f"TIME: {timer} "
    else:
        hud_right= f"ENERGY: {energy} "
    space_padding = 80 - (len(hud_left) + len(hud_right))

    #help and pause menu can only be accessed via normal python input in room 1, so + enter makes it clear to user that they have to enter it in input
    if current_room==1:
        sys.stdout.write(colored('Help (H) Pause (Q) + Enter'.center(80),'red',attrs=['reverse'])+'\n')
    else:
        sys.stdout.write(colored('Help (H) Pause (Q)'.center(80),'red',attrs=['reverse'])+'\n')
    sys.stdout.write(colored(f'{hud_left}{' ' * max(0, space_padding)}{hud_right}\n','red', 'on_white', attrs=['reverse']))
    sys.stdout.write("═" * 80 + "\n")

#checks if player is out of time in room 1
def check_timer():
    if 600-elapsed <= 0:
        print("\033[H\033[J", end="")
        typewriter_print('You have ran out of time.')
        typewriter_print('Forensics have arrived and everyone has evacuated the mansion.')
        typewriter_print('The killer has taken this time to flee.')
        typewriter_print('Game over.')

        print("\033[H\033[J", end="")
        typewriter_print('Oh no, you ran out of time!')
        while True:
            typewriter_print('If you would like to restart the game, enter R')
            typewriter_print('If you would like to quit, enter Q')
            ans=input().strip().lower()
            if ans == 'q':
                #exits entire programme
                sys.exit()
            elif ans == 'r':
                #reruns main.py
                os.execv(sys.executable, [sys.executable] + sys.argv)

#function to run state functions whenever the screen is refreshed for simplicity
def refresh_screen():
    check_terminal_size()
    if current_room == 1:
        check_timer()
    print("\033[H\033[J", end="")
    print_hud(current_objective)

#pauses game and allows player to quit or restart
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