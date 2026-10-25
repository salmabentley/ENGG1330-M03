import tic 
import time
import sys
import main



main.typewriter_print ("You slowly approach the computer, and notice that it has been locked.", delay=0.05)
unlock = input("Do you want to unlock the computer (y/n)? ").strip().lower()
if unlock != "y":
    main.typewriter_print("You decide to leave the computer alone for now.", delay=0.05)
    print()
    sys.exit() #go back to the main exploration loop

main.typewriter_print("You decide to unlock the computer.", delay=0.05)
computer_unlock = False

while True:
    main.typewriter_print("[New Goal] Unlock computer.")
    id = input ("Face ID (1)  Fingerprint (2)  A Challenge (3): ").strip()
    if id == "1":
        main.typewriter_print("You attempt to unlock the computer with Face ID.", delay=0.05)
        main.typewriter_print("You move your face slowly, opposite to the camera.", delay=0.05)
        main.typewriter_print("Checking...", delay=0.05)
        print()
        time.sleep(1)
        print("Unlock failed.")
        time.sleep(1)
        print()
    elif id == "2":
        main.typewriter_print("You attempt to unlock the computer with your fingerprint.", delay=0.05)
        main.typewriter_print("You place your finger on the scanner.", delay=0.05)
        main.typewriter_print("Checking...", delay=0.05)
        print()
        time.sleep(1)
        print("Unlock failed.")
        time.sleep(1)
        print()
    elif id == "3":
        main.typewriter_print("You attempt to unlock the computer with a challenge.", delay=0.05)
        main.typewriter_print("The computer presents you with a tic-tac-toe game.", delay=0.05)
        print()
        tic_result = tic.play()
        if tic_result:
            main.typewriter_print("The computer has been beaten.", delay=0.05)
            time.sleep(1)
            print()
            main.typewriter_print("Unlock succeeded.", delay=0.05)
            computer_unlock = True
            print()
            break
        else:
            main.typewriter_print("You have not won the game", delay=0.05)
            time.sleep(1)
            print()
            main.typewriter_print("Unlock failed.", delay=0.05)
            time.sleep(1)
            print()
    else:
        time.sleep(1)
        print()
        print ("Unlocked failed. Please try again.")
        time.sleep(1)
        print()

main.typewriter_print("The computer lights up and it brings you to Mr.Vance's main browser.", delay=0.05)
main.typewriter_print("You notice that there is an unread email from the mailbox, received at 8:30 pm.", delay=0.05)
main.typewriter_print("Also, you see that the Recycle Bin is currently on. You decide to open the Recycle Bin which stores a video recording and a ZIP file.", delay=0.05)

while computer_unlock:
    main.typewriter_print("[New Goal] Explore the computer", delay=0.05)
    computer_explore = input("Open email (1)  Open ZIP file (2)  Open video recording (3): ").strip()
    if computer_explore == "1":
        main.typewriter_print("You open the email and find a message from Mr.Vance's secretary.", delay=0.05)
        with open("email.txt", "r") as e:
            email_content = e.read()
        print(email_content)
        time.sleep(1)
        print()
        keep_explore = input("Do you want to keep exploring the computer (y/n)? ").strip().lower()
        if keep_explore != "y":
            main.typewriter_print("You decide to stop exploring the computer.", delay=0.05)
            print()
            sys.exit() #go back to the main exploration loop

    elif computer_explore == "2":
        main.typewriter_print("You open the ZIP file and find that it is locked with a password.", delay=0.05)
        zip_lock = input("Do you want to unlock the ZIP file (y/n)? ").strip().lower()
        
        if zip_lock != "y":
            main.typewriter_print("You decide to leave the ZIP file alone for now.", delay=0.05)
        else:
            main.typewriter_print("The password to open this file is the answer to a math question.", delay=0.05)
            print ("[New Goal] Solve the math question: ∫√(tan x) dx from 0 to π/2 ")
            zip_password = input("Enter password: ").strip()
            main.typewriter_print("Checking...", delay=0.05)
            print()
            time.sleep(1)
            
            if zip_password == "something":
                print("Unlock succeeded.")
                with open("zip.txt", "r") as z:
                    zip_content = z.read()
                print()
                print (zip_content)
                time.sleep(1)
                print()
                keep_explore = input("Do you want to keep exploring the computer (y/n)? ").strip().lower()
                if keep_explore != "y":
                    main.typewriter_print("You decide to stop exploring the computer.", delay=0.05)
                    print()
                    sys.exit() #go back to the main exploration loop

            else:
                print("Unlock failed.")
                time.sleep(1)
                print()
            
    
    elif computer_explore == "3":
        main.typewriter_print("You open the video recording and it is playing a man falling off from a 12-story building.", delay=0.05)
        keep_explore = input("Do you want to keep exploring the computer (y/n)? ").strip().lower()
        if keep_explore != "y":
            main.typewriter_print("You decide to stop exploring the computer.", delay=0.05)
            print()
            sys.exit() #go back to the main exploration loop

    else:
        time.sleep(1)
        print()
        print("Invalid option. Please try again.")
        time.sleep(1)
        print()

