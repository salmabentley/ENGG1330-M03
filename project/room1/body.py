
from room1.md import display_md
import state
from state import typewriter_print
import time

def dead_body():
    state.refresh_screen()
    typewriter_print('You check the suit pockets of Thomas Vance\'s dead body')
    typewriter_print('You find a leather wallet engraved with the initials T.V.')
    typewriter_print('You open the wallet and take a look at the cards inside, alongside a photo tucked between two cards')
    
    #create a loop so that player can choose different documents infinitely
    while True: 
        state.current_objective = 'Investigate the wallet'
        state.refresh_screen()
        print('(1) Investigate "Red Cross Card"   \n(2) Investigate credit cards   \n(3) Investigate ID  \n(4) Photo  \n(5) Quit ')
        
        #player can choose different documents by choosing the numbers
        choice = input()

        #first check if the player has pressed h or q to open help or pause menu
        state.check_player_input(choice)

        if choice == '1':
            display_md('documents/red_cross.md') #open different documents with functions from .md
        if choice == '2':
            display_md('documents/bank.md')
        if choice == '3':
            display_md('documents/id.md')
        if choice == '4':
            state.refresh_screen()
            typewriter_print('Photo of Thomas Vance')
            typewriter_print('A photo of Thomas Vance and Peter Lang in a suit, smiling at the camera, putting his arm around Peter Lang.')
            typewriter_print('The photo is dated 1984, and the two men appear to be at a formal event, possibly a graduation ceremony.')
            typewriter_print('[New character & dialogue unlocked]', delay=0.05)
            
            #it marks that the player has already open the photo of Peter Lang and unlock this character + hidden dialogue
            state.photo_found=True 
            state.peter=True
            time.sleep(1)
        if choice == '5':
            return False #break the while loop in the instance that the player wants to exit