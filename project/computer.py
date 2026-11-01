import tic 
import time
from main import typewriter_print

def unlock_computer():
    print("\033[H\033[J", end="")
    typewriter_print ("You slowly approach the computer.", delay=0.05) 
    typewriter_print ("The computer is an old version, probably dating back to a decade ago.", delay=0.05)
    typewriter_print ("You wonder why, as a CEO of a big construction company, Mr.Vance still uses this till now.", delay=0.05)
    typewriter_print ("You move the mouse, hopefully to collect any useful information.", delay=0.05)
    typewriter_print ("And as expected, the computer has been locked...", delay=0.05)
    while True:
        print("\033[H\033[J", end="")
        typewriter_print ("[New Goal] Unlock the computer", delay=0.05)
        id = input ("Face ID (1)  Fingerprint (2)  A Challenge (3)  Exit (4): ").strip() # add exit button
        print("\033[H\033[J", end="")
        if id == "1":
            typewriter_print("You attempt to unlock the computer with your Face ID.", delay=0.05)
            typewriter_print("You move your face slowly, opposite to the camera.", delay=0.05)
            typewriter_print("Checking...", delay=0.1)
            print()
            time.sleep(1)
            print("Unlock failed: Face not recognized\n")
            time.sleep(2)
        elif id == "2":
            typewriter_print("You attempt to unlock the computer with your fingerprint.", delay=0.05)
            typewriter_print("You place your finger on the scanner.", delay=0.05)
            typewriter_print("Checking...", delay=0.1)
            print()
            time.sleep(1)
            print("Unlock failed: Fingerprint not found")
            time.sleep(2)
        elif id == "3":
            typewriter_print("You attempt to unlock the computer by winning a challenge.", delay=0.05)
            typewriter_print("The computer presents you with a tic-tac-toe game.", delay=0.05)
            typewriter_print("You deeply know that this is the only chance for you to unlock the computer.", delay=0.05)
            typewriter_print("And so, you are determine to win this game!", delay=0.05)
            time.sleep(0.5)
            print("\033[H\033[J", end="")
            typewriter_print("[New Goal] Win the tic-tac-toe to unlock the computer.", delay=0.05)
            tic_result = tic.play()
            time.sleep(0.5)
            if tic_result:
                typewriter_print("Checking...", delay=0.1)
                print()
                time.sleep(1)
                typewriter_print("Unlock successful.", delay=0.05)
                return True
            else:
                typewriter_print("Checking...", delay=0.1)
                print()
                time.sleep(1)
                typewriter_print("Unlock failed.", delay=0.05)
        elif id == "4":
            return False
        else:
            print ("Unlocked failed. Please try again.")
            time.sleep(1)


def explore_computer ():
    zip_lock = False
    print("\033[H\033[J", end="")
    typewriter_print("The computer lights up and it brings you to Mr.Vance's main browser.", delay=0.05)
    typewriter_print("You notice that there is an unread email from the mailbox, received at 8:30 pm.", delay=0.05)
    typewriter_print ("You also see the Recycle Bin is currently on and decide to open it.", delay=0.05)
    typewriter_print("The bin stores a video recording and a ZIP file, which have been deleted just a couple of hours ago.", delay =0.05)
    typewriter_print("You wonder why...", delay=0.05)

    while True:
        print("\033[H\033[J", end="")
        typewriter_print("[New Goal] Explore the computer", delay=0.05)
        computer_explore = input("Open email (1)  Open ZIP file (2)  Open video recording (3)  Exit (4): ").strip()
        if computer_explore == "1":
            typewriter_print("You open the email and find a message from Mr.Vance's secretary.", delay=0.05)
            with open("email.md", "r") as e:
                email_content = e.read()
            print("\033[H\033[J", end="")
            print(email_content)
            next = input("Press Enter to continue ")
        elif computer_explore == "2":
            if not zip_lock:
                typewriter_print("You open the ZIP file and find that it is locked with a password.", delay=0.05)
                zip_lock = input("Do you want to unlock the ZIP file (y/n)? ").strip().lower()
                if zip_lock != "y":
                    typewriter_print("You decide to leave the ZIP file alone for now.", delay=0.05)
                else:
                    typewriter_print("The password to open this file is the answer to a math question.", delay=0.05)
                    print("\033[H\033[J", end="")
                    typewriter_print ("[New Goal] Solve the math question to unzip the file: ∫√(tan x) dx from 0 to π/2", delay=0.05)
                    typewriter_print ("Hint: pi, sqrt(), /", delay=0.05)
                    zip_password = input("Enter password: ").strip()
                    typewriter_print("Checking...", delay=0.1)
                    print()
                    time.sleep(1)
                    if zip_password == "pi/sqrt(2)":
                        zip_lock = True
                        typewriter_print("Unlock successful.", delay=0.05)
                    else:
                        print("Unlock failed.")
                        time.sleep(1)
            if zip_lock:
                with open("zip.md", "r") as z:
                    zip_content = z.read()
                print("\033[H\033[J", end="")
                print (zip_content)
                next = input("Press Enter to continue ")
                
        elif computer_explore == "3":
            typewriter_print("You open the video recording and it is playing a man falling off from a 12-story building.", delay=0.05)
            next = input("Press Enter to continue ")
        elif computer_explore == "4":
            return False
        else:
            print("Invalid option. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    if unlock_computer():
        explore_computer()