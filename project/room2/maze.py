
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

import keyboard
from termcolor import colored
from .. import state
from .eleanor_lan import eleanor
from .gabrielle import gabrielle
from .GeorgeTam import george
from .PeterLang import peter
from .accusation import accusation

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


def is_movable(x,y):
    if maze[y][x] == '.':
        return True
    else:
        if maze[y][x] == '&':
            george()
            draw_maze()
        elif maze[y][x] == '#':
            eleanor()
            draw_maze()
        elif maze[y][x] == '%':
            peter()
            draw_maze()
        elif maze[y][x] == '@':
            gabrielle()
            draw_maze()
        return False

def check_energy():
    if state.energy-1 <=0:
        return False
    else:
        return True

def move():
    global posy
    global posx
    posy = 1
    posx = 14
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            moved = False
            
            if event.name == 'w':
                if is_movable(posx, posy - 1):
                    maze[posy][posx] = '.'
                    posy -= 1
                    maze[posy][posx] = 'x'
                    moved = True
                    state.energy-=state.energy_decrease
            elif event.name == 'a':
                if is_movable(posx - 2, posy):
                    if check_energy():
                        maze[posy][posx] = '.'
                        posx -= 2
                        maze[posy][posx] = 'x'
                        moved = True
                        state.energy-=state.energy_decrease
            elif event.name == 's':
                if is_movable(posx, posy + 1):
                    maze[posy][posx] = '.'
                    posy += 1
                    maze[posy][posx] = 'x'
                    moved = True
                    state.energy-=state.energy_decrease
            elif event.name == 'd':
                if is_movable(posx + 2, posy):
                    maze[posy][posx] = '.'
                    posx += 2
                    maze[posy][posx] = 'x'
                    moved = True
                    state.energy-=state.energy_decrease
            elif event.name == 'p':
                state.refresh_screen()
                state.typewriter_print('Are you sure you want to proceed to the final accusation? (y/n)')
                while True:
                    ans=input()
                    if ans.lower().strip() == 'y':
                        accusation()
                        return
                    elif ans.lower().strip() == 'n':
                        break
                draw_maze()
            
            if moved:
                draw_maze()
                if not check_energy():
                    exit('Game over')

def draw_maze():
    # print("\033[H\033[J", end="")
    state.refresh_screen()

    for row in maze:
        for element in row:
            if element.isalpha():
                if element == 'x':
                    print(colored(element, 'red', attrs=['bold']), end='')
                else:
                    print(colored(element, 'white', attrs=['bold']), end='')
            else:
                if element == '%':
                    print(colored(element, 'blue'), end='')
                elif element == '@':
                    print(colored(element, 'yellow'), end='')
                elif element == '&':
                    print(colored(element, 'magenta'), end='')
                elif element == '#':
                    print(colored(element, 'green'), end='')
                else:
                    print(element, end='')
        print()
    print('═'*80)
    print(f'{colored('%','blue')} {'Peter Lang' if state.photo  else '???'}   {colored('@','yellow')} Ms. Gabrielle  {colored('&','magenta')} George Tam   {colored('#','green')} Eleanor Lan')
    print('Use WASD to move, P to end the maze and convict someone.')

draw_maze()
move()
