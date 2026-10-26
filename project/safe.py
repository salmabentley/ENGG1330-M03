import time
from introduction import typewriter_print
from md import display_md

def play_safe():
    print("\033[H\033[J", end="")
    time.sleep(1)
    typewriter_print('You approach the safe, its red light blinking ominously.', delay=0.05)
    typewriter_print('Above the safe, you see a poster showing all the blood types.', delay=0.05)
    typewriter_print('Looking down, you see a keypad with numbers 0-9, with 3 small letters under each number', delay=0.05)
    res = get_yes_no('Would you like to enter a code? Yes (y) No (n)')
    if (not res):
        return False
    else:
        while True:
            print("\033[H\033[J", end="")
            print_keypad()
            code=input('Enter the code:  ')
            if (code!='2220'):
                typewriter_print('The safe beeps angrily, rejecting your code.', delay=0.05)
                res = get_yes_no('Would you like to re-enter another code? Yes (y) No (n)')
                if (not res):
                    return False
            else:
                print("\033[H\033[J", end="")
                typewriter_print('*CLICK* The red light turns off and the heavy lock opens, revealing its contents.', delay=0.05)
                return True

def safe_contents():
    print("\033[H\033[J", end="")
    typewriter_print('Inside the safe, you see a stack of money, a news paper, and a file.', delay=0.05)
    while True:
        typewriter_print('What would you like to do? Inspect money (1) Read newspaper article (2) Examine file (3) Exit safe (d)',delay=0.03)
        choice = input()
        if choice =='1':
            print("\033[H\033[J", end="")
            typewriter_print('You pick up the money and notice a sticky note placed on top of the stack. It reads:', delay=0.04)
            typewriter_print('"For Eleanor"', delay=0.1)
            typewriter_print('You count the money and find that it is an exceptionally large sum, enough to sustain a family for a few years', delay=0.04)
            typewriter_print('You put the money back in the safe.', delay=0.04)
            print("\033[H\033[J", end="")
        elif choice == '2':
            print("\033[H\033[J", end="")
            typewriter_print('You pick up the newspaper and read the article.', delay=0.04)
            display_md('./project/documents/news.md')
            print("\033[H\033[J", end="")
        elif choice == '3':
            print("\033[H\033[J", end="")
            typewriter_print('You pick up the file and examine it.', delay=0.04)
            typewriter_print('There seem to be documents regarding an investigation.', delay=0.04)
            typewriter_print('You begin reading through the documents.', delay=0.04)
            display_md('./project/documents/negligence_docs.md')
            print("\033[H\033[J", end="")
        elif choice.lower() == 'd':
            print("\033[H\033[J", end="")
            typewriter_print('You close the safe and step away.', delay=0.04)
            break



def get_yes_no(prompt):
    while True:
        typewriter_print(prompt, delay=0.02)
        res = input().strip().lower()
        if res == 'y':
            return True
        elif res =='n':
            return False
        else:
            typewriter_print('Invalid input. Please enter "y" for yes or "n" for no.', delay=0.02)

def print_keypad():
    print('\nKeypad:\n')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~ 1(-) ~~ 2(ABC) ~~ 3(DEF) ~~')
    print('~ 4(GHI) ~~ 5(JKL) ~~ 6(MNO) ~')
    print('~ 7(PQRS) ~ 8(TUV) ~ 9(WXYZ) ~')
    print('~~~~ * ~~~~~ 0(+) ~~~~~ # ~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

