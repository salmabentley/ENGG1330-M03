import sys
import time

# GLOBAL VARIABLES
safe_unlocked=False
computer_unlocked=False
current_objective = ''
body_investigated=False
computer_investigated = False
safe_investigated = False
start=0
timer=0

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
    hud_right = f"TIME: {timer} "
    space_padding = 80 - (len(hud_left) + len(hud_right))
    # Print header with reverse highlight & red text
    sys.stdout.write(f"\033[7m\033[1m\033[91m{hud_left}{' ' * max(0, space_padding)}{hud_right}\033[0m\n")
    sys.stdout.write("═" * 80 + "\n")

def refresh_screen():
    print("\033[H\033[J", end="")
    print_hud(current_objective)