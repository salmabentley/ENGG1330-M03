import sys
import termios
import tty
import select
import state
import time
from room2.eleanor_lan import eleanor
from room2.gabrielle import gabrielle
from room2.GeorgeTam import george
from room2.PeterLang import peter
from room2.accusation import accusation
from room1.md import display_md

try:
    from termcolor import colored
except ImportError:
    _FG = {
        "dark_grey": "\033[90m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
    }
    _BG = {
        "on_white": "\033[47m",
        "on_red": "\033[41m",
    }
    _ATTR = {
        "reverse": "\033[7m",
        "bold": "\033[1m",
    }

    def colored(text, color=None, on_color=None, attrs=None):
        codes = []
        if color in _FG:
            codes.append(_FG[color])
        if on_color in _BG:
            codes.append(_BG[on_color])
        if attrs:
            for attr in attrs:
                if attr in _ATTR:
                    codes.append(_ATTR[attr])
        if not codes:
            return str(text)
        return f"{''.join(codes)}{text}\033[0m"

#array to store our mansion grid
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

# dots - movable spaces in the mansion
# | or -- are walls which cannot be moved
# x is the player
# any other special symbol like % and @ are interactable npcs


#checks if the cell the player is moving to is movable
def is_movable(x, y, fd, old_settings):
    cell = maze[y][x]
    if cell == '.':
        return True
    else:
        # Temporarily restore standard terminal mode for cutscene dialogues & inputs
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        # checks if the cell is an npc
        if cell == '&':
            george()
        elif cell == '#' and not state.eleanor_disabled:    #checks whether eleanor has been disabled due to poor dialogue choices
            eleanor()
        elif cell == '%':
            peter()
        elif cell == '@' and not state.gabrielle_disabled:
            gabrielle()
            
        # Redraw maze and switch back to cbreak mode for real-time movement
        draw_maze()
        tty_mode = termios.tcgetattr(fd)
        # Re-apply cbreak behavior
        import tty
        tty.setcbreak(fd)
        
        return False

#check whether the player has run out of energy
def check_energy():
    if state.energy <=0:
        return False
    else:
        return True

#function to allow players to move around the mansion
def move():
    global posy
    global posx

    #starting position of the player (outside office)
    posy = 1
    posx = 14

    #render the maze
    draw_maze()

    #allows for continuous data stream to capture wasd keys without curses or standard python input (which requires players to press enter)
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

                        #replace previous cell with a dot
                        maze[posy][posx] = '.'
                        posy -= 1

                        #update moved cell to x
                        maze[posy][posx] = 'x'
                        moved = True

                        #subtract energy for each move
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

                    #allow players to proceed to the final accusation or continue exploring the mansion
                    while True:
                        ans = input()
                        if ans.lower().strip() == 'y':
                            #play accusation and end the game
                            accusation()
                            return
                        elif ans.lower().strip() == 'n':
                            #re enter maze loop and rerender the maze
                            break
                    draw_maze()
                    
                    # Re-enable cbreak mode after the menu closes
                    tty.setcbreak(fd)
                elif ch=='q':
                    #stop continuous keyboard polling so that normal python input works for the pause menu
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                    state.pause_game()
                    tty.setcbreak(fd)
                    draw_maze()

                elif ch=='h':
                    #stop continuous keyboard polling so that normal python input works for the help menu
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

                        #directly leads players to the final accusation if they run out of energy
                        accusation()
                        
    finally:
        # Always guarantee terminal settings are restored on exit or Ctrl+C
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def draw_maze():
    state.refresh_screen()

    # rendering the maze
    for row in maze:
        print(' '*16, end='')   #centers the maze
        for element in row:
            if element.isalpha():
                #applies styling to the npcs and player to make it pop
                if element == 'x':
                    print(colored(element, 'red', attrs=['bold']), end='')
                else:
                    print(colored(element, 'white', attrs=['bold']), end='')
            else:
                if element == '%':
                    print(colored(element, 'blue'), end='')
                elif element == '@' and not state.gabrielle_disabled:   #do not add styling to disabled npcs
                    print(colored(element, 'yellow'), end='')
                elif element == '&':
                    print(colored(element, 'magenta'), end='')
                elif element == '#' and not state.eleanor_disabled:
                    print(colored(element, 'green'), end='')
                else:
                    print(element, end='')
        print()
    print('═'*80)

    #render the legend with styling
    print(f"{colored('%','blue')} {'Peter Lang' if state.peter else '???'} {colored('@','yellow') if not state.gabrielle_disabled else colored('@', 'dark_grey')} {colored('Ms. Gabrielle [Unreachable]', 'dark_grey') if state.gabrielle_disabled else ('Ms. Gabrielle' if state.gabrielle else '???')} {colored('&','magenta')} {'George Tam' if state.george else '???'} {colored('#','green' if not state.eleanor_disabled else 'dark_grey')} {colored('Eleanor Lan [Unreachable]', 'dark_grey') if state.eleanor_disabled else 'Eleanor Lan' if state.eleanor else '???'}")
    print('Use WASD to move, P to end the maze and convict someone.')

