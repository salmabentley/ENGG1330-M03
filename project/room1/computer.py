from room1 import tic       #import the tic_tac_toe game from room1 file
import time     #import time module from Python library to create pulses between dialogues, like loading, processing,... 
from room1.md import display_md     #import the display_md function to display the text in favorable format
import state        #get access to clean screen, displaying time and objective in the terminal functions
from state import typewriter_print      #display text character by character similar like real game

def unlock_computer():      #return a boolean expression, ensuring player unlocks the computer first before they can explore the computer
    state.refresh_screen()      #clean the screen      
    typewriter_print ("You slowly approach the computer.", delay=0.05) 
    typewriter_print ("The computer is an old version, probably dating back to a decade ago.", delay=0.05)
    typewriter_print ("You wonder why, as a CEO of a big construction company, Mr.Vance still uses this till now.", delay=0.05)
    typewriter_print ("You move the mouse, hopefully to collect any useful information.", delay=0.05)
    typewriter_print ("And as expected, the computer has been locked...", delay=0.05)
    while True:     #this loop ensures that the challenge will repeat until the player successfully unlocks the computer, return True to the function unlock_computer
        state.current_objective='Unlock the computer'       #display the objective on the terminal
        state.refresh_screen()
        typewriter_print ("[New Goal] Unlock the computer", delay=0.05)
        id = input ("Face ID (1)  Fingerprint (2)  A Challenge (3)  Exit (4): ").strip()        #choices for user to interact with the game, the input will be strip() to match the format when player accidently types a space bar
        state.check_player_input(id)

        state.refresh_screen()
        if id == "1":       #when user inputs 1, the following diaglogue will appear
            typewriter_print("You attempt to unlock the computer with your Face ID.", delay=0.05)
            typewriter_print("You move your face slowly, opposite to the camera.", delay=0.05)
            typewriter_print("Checking...", delay=0.1)
            print()
            time.sleep(1)
            print("Unlock failed: Face not recognized\n")       #after this line is printed, it will loop again in the while True, showing the options to unlock computer
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
            time.sleep(0.5)
            state.current_objective = 'Win the tic-tac-toe to unlock the computer'
            state.refresh_screen()
            typewriter_print("[New Goal] Win the tic-tac-toe to unlock the computer.", delay=0.05)
            tic_result = tic.play()     #the tic.play() function will run, displaying the game and return True if user wins and False otherwise. This boolean is stored in the variable tic_result to unlock the following dialogues
            time.sleep(0.5)
            if tic_result:      #if tic_result is True meaning the player wins the game, the computer is unlocked and the function unlock_computer() will return True
                typewriter_print("Checking...", delay=0.1)
                print()
                time.sleep(1)
                typewriter_print("Unlock successful.", delay=0.05)
                explore_computer()
                return True     #this line ends the loop, the function returns True and this is going to unlock 
            else:
                typewriter_print("Checking...", delay=0.1)
                print()
                time.sleep(1)
                typewriter_print("Unlock failed.", delay=0.05)
        elif id == "4":
            return False        #in case the player does not want to unlock the computer, the function will return False and end the loop
        else:       #in case user does not input the correct format answer, the user will continue to stay in the loop
            print ("Unlocked failed. Please try again.")
            time.sleep(1)


def explore_computer():
    zip_unlock = False      #local variable to use within the function. If zip file is unlocked return True, then the player can access the content inside
    state.refresh_screen()
    typewriter_print("The computer lights up and it brings you to Mr.Vance's main browser.", delay=0.05)
    typewriter_print("You notice that there is an unread email from the mailbox, received at 8:30 pm.", delay=0.05)
    typewriter_print ("You also see the Recycle Bin is currently on and decide to open it.", delay=0.05)
    typewriter_print("The bin stores a video recording and a ZIP file, which have been deleted just a couple of hours ago.", delay =0.05)
    typewriter_print("You wonder why...", delay=0.05)

    typewriter_print("[New Goal] Explore the computer", delay=0.05)
    while True:
        state.current_objective = 'Explore the computer'
        state.refresh_screen()
        computer_explore = input("Open email (1)  Open ZIP file (2)  Open video recording (3)  Exit (4): ").strip()
        state.check_player_input(computer_explore)

        if computer_explore == "1":
            typewriter_print("You open the email and find a message from Mr.Vance's secretary.", delay=0.05)
            display_md('documents/email.md')        #displays the email.md under the document file
        elif computer_explore == "2":
            if not zip_unlock:      #if the zip_lock is False, so the zip has not been unlocked yet then the player requires to unlock it first
                typewriter_print("You open the ZIP file and find that it is locked with a password.", delay=0.05)
                user = input("Do you want to unlock the ZIP file (y/n)? ").strip().lower()
                state.check_player_input(user)

                if user == "n":
                    typewriter_print("You decide to leave the ZIP file alone for now.", delay=0.05)
                else:
                    typewriter_print("The password to open this file is the answer to a math question.", delay=0.05)
                    state.current_objective = 'Solve the math question to unzip the file'
                    state.refresh_screen()
                    typewriter_print ("[New Goal] Solve the math question to unzip the file: ∫√(tan x) dx from 0 to π/2", delay=0.05)
                    typewriter_print ("Hint: pi, sqrt(), /", delay=0.05)
                    zip_password = input("Enter password: ").strip()
                    state.check_player_input(zip_password)

                    typewriter_print("Checking...", delay=0.1)
                    print()
                    time.sleep(1)
                    if zip_password == "pi/sqrt(2)":
                        zip_unlock = True
                        typewriter_print("Unlock successful.", delay=0.05)
                    else:
                        print("Unlock failed.")
                        time.sleep(1)
            if zip_unlock:      #if the zip_unlock is now True, the zip.md will open. Even if the user exits the computer and then comes back, the state of zip_unlock will stay True so the content will display without having the player to repeat the unlocking step above
                display_md('documents/zip.md')
        elif computer_explore == "3":
            typewriter_print("You open the video recording and it is playing a man falling off from a 12-story building.", delay=0.05)
        elif computer_explore == "4":
            return False
        else:
            print("Invalid option. Please try again.")
            time.sleep(1)
