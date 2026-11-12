
from room1.md import display_md
import state
from state import typewriter_print
import time

def dead_body():
    state.refresh_screen()
    typewriter_print('You check the suit pockets of Thomas Vance\'s dead body', delay=0.05)
    typewriter_print('You find a leather wallet engraved with the initials T.V.', delay=0.05)
    typewriter_print('You open the wallet and take a look at the cards inside, alongside a photo tucked between two cards', delay=0.05)
    while True:
        state.current_objective = 'Investigate the wallet'
        state.refresh_screen()
        typewriter_print('Investigate "Red Cross Card" (1)  Investigate credit cards (2)  Investigate ID (3) Photo (4) Quit (5)', delay=0.02)
        choosing_number = input()
        state.check_player_input(choosing_number)

        if choosing_number == '1':
            display_md('documents/red_cross.md')
        if choosing_number == '2':
            display_md('documents/bank.md')
        if choosing_number == '3':
            display_md('documents/id.md')
        if choosing_number == '4':
            state.refresh_screen()
            typewriter_print('Photo of Thomas Vance', delay=0.05)
            typewriter_print('A photo of Thomas Vance and Peter Lang in a suit, smiling at the camera, putting his arm around Peter Lang.', delay=0.05)
            typewriter_print('The photo is dated 1984, and the two men appear to be at a formal event, possibly a graduation ceremony.', delay=0.05)
            typewriter_print('[New character & dialogue unlocked]', delay=0.05)
            state.photo_found=True
            state.peter=True
            time.sleep(1)
        if choosing_number == '5':
            return False