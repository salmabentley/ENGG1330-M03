import sys
import time
from termcolor import colored


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
    elapsed=time.time()-start
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