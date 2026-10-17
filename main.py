import sys
import time

def typewriter_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 
    time.sleep(1)



def get_name():
    print("\033[H\033[J", end="")
    time.sleep(1)
    typewriter_print("Welcome to group M03's project.", delay=0.05)
    typewriter_print("Please enter your name: ", delay=0.05)
    global name
    name=input()
    typewriter_print(f'Welcome, detective {name}.', delay=0.05)
    time.sleep(1)

def play_intro():
    print("\033[H\033[J", end="")
    time.sleep(1)
    typewriter_print('You have been invited to a party at a mansion by your former client, Thomas Vance.', delay=0.05)
    typewriter_print('Rain splatters heavily against the stained glass windows as music and laughter echo from the grand ballroom.', delay=0.05)
    typewriter_print('Eight months ago, Vance hired you to clear his name in a minor corporate dispute.', delay=0.05)
    typewriter_print('Tonight, he invited you as a guest of honor... or perhaps as insurance', delay=0.05)
    print("\033[H\033[J", end="")
    time.sleep(1)
    typewriter_print('A sharp scream cuts through the music from the second-floor study.', delay=0.05)
    typewriter_print('You rush upstairs.', delay=0.05)
    typewriter_print('Guests and staff are standing in the hallway, shaken.', delay=0.05)
    typewriter_print('You push open the heavy mahogany door.', delay=0.05)
    print("\033[H\033[J", end="")
    time.sleep(1)
    typewriter_print('Thomas Vance lays in a pool of his own blood in the centre of the room.', delay=0.05)
    typewriter_print('Peter Lang crouches next to him, visibly shaken.', delay=0.05)
    typewriter_print('You remember seeing him when investigating Vance Construction.', delay=0.05)
    typewriter_print('You ask him to leave the scene so that you can investigate further.', delay=0.05)
    print("\033[H\033[J", end="")
    time.sleep(1)
    typewriter_print('Tucked in a corner, you spot an electronic safe, blinking red.', delay=0.05)
    typewriter_print('Vance\'s computer is still on, seemingly on some sort of game.', delay=0.05)
    typewriter_print('[New Goal] Investigate the room.', delay=0.05)
    typewriter_print('Investigate body (1)  Go to computer (2)  Go to the safe (3)', delay=0.05)

    #you have been invited to a party at a mansion by your former client, Thomas Vance. Rain heavy against the stained glass windows as music and laughter echo from the grand ballroom. Eight months ago, Vance hired you to clear his name in a minor corporate dispute. Tonight, he invited you as a guest of honor... or perhaps as insurance. A sharp scream cuts through the music from the second-floor study.You rush upstairs. Guests are standing in the hallway, shaken.You push open the heavy mahogany door. Thomas Vance is slumping over his desk, motionless. Beside his hand sits an electronic safe, blinking red.


if __name__ == "__main__":
    get_name()
    play_intro()

#salfdjewqjfiwqjflwjlfjalfew