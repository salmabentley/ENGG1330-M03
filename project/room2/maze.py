
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

maze=[
    list('|---------------------------------------------|'),
    list('|door | x . . . . . . . . . . . . |kitchen| . |'),
    list('|-------| . |-----------------| . |-------| . |'),
    list('|office | . | . . . . . . . . | . | . . . | . |'),
    list('|-------| . | . . |library| . | . |---| . . . |'),
    list('| . . . | . | . . |-----------| . | . . . . . |'),
    list('| . . . | . | . . | . . . . . . . . . . . . . |'),
    list('| . . . . . . . . . . . . . . | . . . . . . . |'),
    list('|-------| . |-----------------| . |-----------|'),
    list('|fitness| . . . . . . . . . . | . | . . | . % |'),
    list('| room  | . | . & . . . . . . | . | . . | . . |'),
    list('|-------| . | . . . . . . . . | . | . . | . . |'),
    list('| . | . | . | . |ballroom | . | . |-| . | . |-|'),
    list('| . | . | . | . . . . . . . . . . | . . . . . |'),
    list('| . . . . . |-----------------| . . . |toilet |'),
    list('|-------| . . . . . . . . . . . . . |---------|'),
    list('| . . . . . . . . . . . . . . . . . |         |'),
    list('|-----------------| . | . |---------|         |'),
    list('| conference room | . | . | bedroom  ----|    |'),
    list('|-----------------| . | . |-------------------|'),
    list('| . . . . . . . . . . | . | . . . . . . . . . |'),
    list('| # . . . . . . . | . | . | . . . . . . . . . |'),
    list('|-----------------| . | . . . . . |  bathroom |'),
    list('| . . . . . . . . | . | . . |-----------------|'),
    list('| . . . . . . . . . . | . . . . . . . . . . @ |'),
    list('|---------------------------------------------|')
]


def is_movable(x,y):
    if maze[y][x] == '.':
        return True
    else:
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
    posx = 8
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
                    state.energy-=1
            elif event.name == 'a':
                if is_movable(posx - 2, posy):
                    if check_energy():
                        maze[posy][posx] = '.'
                        posx -= 2
                        maze[posy][posx] = 'x'
                        moved = True
                        state.energy-=1
            elif event.name == 's':
                if is_movable(posx, posy + 1):
                    maze[posy][posx] = '.'
                    posy += 1
                    maze[posy][posx] = 'x'
                    moved = True
                    state.energy-=1
            elif event.name == 'd':
                if is_movable(posx + 2, posy):
                    maze[posy][posx] = '.'
                    posx += 2
                    maze[posy][posx] = 'x'
                    moved = True
                    state.energy-=1
            
            if moved:
                draw_maze()
                if not check_energy():
                    exit('Game over')

def draw_maze():
    print("\033[H\033[J", end="")

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
                    print(colored(element, 'blue'), end='')
                else:
                    print(element, end='')
        print()
            

draw_maze()
move()
