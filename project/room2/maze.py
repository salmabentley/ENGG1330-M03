
# |---------------------------------------------|
# |door | . . . . . . . . . . . . . |kitchen| . |
# |-------| . |-----------------| . |-------| . |
# |office | . | . . . . . . . . | . | . . . | . |
# |-------| . | . . |library| . | . |---| . . . |
# | . . . | . | . . |-----------| . | . . . . . |
# | . . . | . | . . | . . . . . . . . . . . . . |
# | . . . . . . . . . . . . . . | . . . . . . . |
# |-------| . |-----------------| . |-----------|
# |fitness| . . . . . . . . . . | . | . . | . x |
# | room  | . | . x . . . . . . | . | . . | . . |
# |-------| . | . . . . . . . . | . | . . | . . |
# | . | . | . | . |ballroom | . | . |-| . | . |-|
# | . | . | . | . . . . . . . . . . | . . . . . |
# | . . . . . |-----------------| . . . |toilet |
# |-------| . . . . . . . . . . . . . |---------|
# | . . . . . . . . . . . . . . . . . |         |
# |-----------------| . | . |---------|         |
# | conference room | . | . | bedroom  ----|    |
# |-----------------| . | . |-------------------|
# | . . . . . . . . . . | . | . . . . . . . . . |
# | x . . . . . . . | . | . | . . . . . . . . . |
# |-----------------| . | . . . . . |  bathroom |
# | . . . . . . . . | . | . . |-----------------|
# | . . . . . . . . . . | . . . . . . . . . . x |
# |---------------------------------------------|

import sys
import termios
import tty
import select
from termcolor import colored
import state
import time
from room2.eleanor_lan import eleanor
from room2.gabrielle import gabrielle
from room2.GeorgeTam import george
from room2.PeterLang import peter
from room2.accusation import accusation
from room1.md import display_md

maze=[
    list('|---------------------------------------------|'),
    list('|library| . . x |office | . . . . |  kitchen  |'),
    list('|-------| . |-----------------| . |-----------|'),
    list('|fitness| . . . . . . . . . . | . | . . | . % |'),
    list('| room  | . | . & . . . . . . | . | . . | . . |'),
    list('|-------| . | . . . . . . . . | . | . . | . . |'),
    list('| . | . | . | . |ballroom | . | . |-| . | . |-|'),
    list('| . | . | . | . . . . . . . . . . | . . . . . |'),
    list('| . . . . . |-----------------| . . . |toilet |'),
    list('|-------| . . . . . . . . . . . . . |---------|'),
    list('|-----------------| . | . |---------|         |'),
    list('| conference room | . | . | bedroom  ----|    |'),
    list('|-----------------| . | . |-------------------|'),
    list('| # . . . . . . . . . | . | . . . . . . . . . |'),
    list('|-----------------| . | . . . . . |  bathroom |'),
    list('| . . . . . . . . | . | . . |-----------------|'),
    list('| . . . . . . . . . . | . . . . . . . . . . @ |'),
    list('|---------------------------------------------|')
]


def is_movable(x, y, fd, old_settings):
    cell = maze[y][x]
    if cell == '.':
        return True
    else:
        # Temporarily restore standard terminal mode for cutscene dialogues & inputs
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        
        if cell == '&':
            george()
        elif cell == '#' and not state.eleanor_disabled:
            eleanor()
        elif cell == '%':
            peter()
        elif cell == '@':
            gabrielle()
            
        # Redraw maze and switch back to cbreak mode for real-time movement
        draw_maze()
        tty_mode = termios.tcgetattr(fd)
        # Re-apply cbreak behavior
        import tty
        tty.setcbreak(fd)
        
        return False
def check_energy():
    if state.energy <=0:
        return False
    else:
        return True


# (Keep your maze list, is_movable, check_energy, and draw_maze as they are)

def move():
    global posy
    global posx
    posy = 1
    posx = 14
    draw_maze()

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    
    try:
        # Enable cbreak mode once so it stays active while navigating the maze
        tty.setcbreak(fd)
        
        while True:
            # Poll stdin for a keypress
            if select.select([sys.stdin], [], [], 0.1)[0]:
                ch = sys.stdin.read(1).lower()
                moved = False
                
                if ch == 'w':
                    if is_movable(posx, posy - 1, fd, old_settings):
                        maze[posy][posx] = '.'
                        posy -= 1
                        maze[posy][posx] = 'x'
                        moved = True
                        state.energy -= state.energy_decrease
                elif ch == 'a':
                    if is_movable(posx - 2, posy, fd, old_settings):
                        if check_energy():
                            maze[posy][posx] = '.'
                            posx -= 2
                            maze[posy][posx] = 'x'
                            moved = True
                            state.energy -= state.energy_decrease
                elif ch == 's':
                    if is_movable(posx, posy + 1, fd, old_settings):
                        maze[posy][posx] = '.'
                        posy += 1
                        maze[posy][posx] = 'x'
                        moved = True
                        state.energy -= state.energy_decrease
                elif ch == 'd':
                    if is_movable(posx + 2, posy, fd, old_settings):
                        if check_energy():
                            maze[posy][posx] = '.'
                            posx += 2
                            maze[posy][posx] = 'x'
                            moved = True
                            state.energy -= state.energy_decrease
                elif ch == 'p':
                    # Temporarily restore normal terminal mode so input() works cleanly for 'P'
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                    
                    state.refresh_screen()
                    state.typewriter_print('Are you sure you want to proceed to the final accusation? (y/n)')
                    while True:
                        ans = input()
                        if ans.lower().strip() == 'y':
                            accusation()
                            return
                        elif ans.lower().strip() == 'n':
                            break
                    draw_maze()
                    
                    # Re-enable cbreak mode after the menu closes
                    tty.setcbreak(fd)
                elif ch=='q':
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                    state.pause_game()
                    tty.setcbreak(fd)
                    draw_maze()

                elif ch=='h':
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                    display_md('documents/help.md')
                    tty.setcbreak(fd)
                    draw_maze()


                
                if moved:
                    draw_maze()
                    if not check_energy():
                        state.refresh_screen()
                        state.typewriter_print('You have ran out of energy.')
                        state.typewriter_print('You no longer can interact with the people in the mansion.')
                        state.typewriter_print('It is now up to you to pick someone to arrest with the clues you have gathered thus far.')
                        time.sleep(1)
                        accusation()
                        
    finally:
        # Always guarantee terminal settings are restored on exit or Ctrl+C
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def draw_maze():
    # print("\033[H\033[J", end="")
    state.refresh_screen()

    for row in maze:
        print(' '*16, end='')
        for element in row:
            if element.isalpha():
                if element == 'x':
                    print(colored(element, 'red', attrs=['bold']), end='')
                else:
                    print(colored(element, 'white', attrs=['bold']), end='')
            else:
                if element == '%':
                    print(colored(element, 'blue'), end='')
                elif element == '@' and not state.gabrielle_disabled:
                    print(colored(element, 'yellow'), end='')
                elif element == '&':
                    print(colored(element, 'magenta'), end='')
                elif element == '#' and not state.eleanor_disabled:
                    print(colored(element, 'green'), end='')
                else:
                    print(element, end='')
        print()
    print('═'*80)
    print(f"{colored('%','blue')} {'Peter Lang' if state.peter else '???'} {colored('@','yellow') if not state.gabrielle_disabled else colored('@', 'dark_grey')} {colored('Ms. Gabrielle [Unreachable]', 'dark_grey') if state.gabrielle_disabled else ('Ms. Gabrielle' if state.gabrielle else '???')} {colored('&','magenta')} {'George Tam' if state.george else '???'} {colored('#','green' if not state.eleanor_disabled else 'dark_grey')} {colored('Eleanor Lan [Unreachable]', 'dark_grey') if state.eleanor_disabled else 'Eleanor Lan' if state.eleanor else '???'}")
    print('Use WASD to move, P to end the maze and convict someone.')

