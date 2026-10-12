import sys
import time

def typewriter_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 

def play_intro():
    # Clear screen (optional, creates a clean slate)
    print("\033[H\033[J", end="")
    
    time.sleep(1)
    
    # Backstory narrative
    typewriter_print("Hello world", delay=0.05)


if __name__ == "__main__":
    play_intro()