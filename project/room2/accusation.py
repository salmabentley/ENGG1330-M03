from .. import state
from ..state import typewriter_print
import time

def accusation():
    state.current_objective='Arrest someone.'
    state.refresh_screen()
    typewriter_print('The rain outside begins pouring harder.')
    typewriter_print('Faint sounds of thunder can be heard in the distance.')
    typewriter_print('The old floors of the mansion reverbrate with each strike of lightning.')
    typewriter_print('You enter the ballroom.')
    state.refresh_screen()
    typewriter_print('Quiet individual whispers bounce against the walls.')
    typewriter_print('It fills the room with anticipation.')
    typewriter_print('The police have arrived outside the mansion.')
    typewriter_print('It is time to put someone in handcuffs.')
    state.refresh_screen()
    typewriter_print('Who do you think killed Thomas Vance? This decision cannot be changed.')
    print('(1) Eleanor Lan\n(2) George Tam\n(3) Peter Lang\n (4) Ms. Gabrielle')
    while True:
        ans=input()
        if ans=='1':
            pass

def play_accusation(character):
    state.current_objective=f'Arrest {character}'
    state.refresh_screen()
    typewriter_print(f'You find {character} in the crowd.')
    if character=='Gabrielle Iang':
        typewriter_print('She is still holding the cigarette she was smoking earlier.')
        typewriter_print('You approach her, gun holstered and handcuffs visible.')
        typewriter_print('A hint of fear flashes in her eyes.')
    elif character=='George Tam':
        typewriter_print('He is in the same place as when you first met him.')
        typewriter_print('You approach him, gun holstered and handcuffs visible.')
        typewriter_print('He looks confused, almost bewildered.')
    elif character=='Peter Lang':
        typewriter_print('He seems to have helped himself to another glass of whiskey.')
        typewriter_print('You approach him, gun holstered and handcuffs visible.')
        typewriter_print('He does not seem to notice, staring off into the distance instead.')
    else:
        typewriter_print('She is on her phone, seemingly texting someone.')
        typewriter_print('You approach her, gun holstered and handcuffs visible.')
        typewriter_print('She looks up from her phone, in shock to see you.')

    state.refresh_screen()
    typewriter_print(f'You: {character}, you are under arrest under suspicion for the murder of Thomas Vance.')
    typewriter_print('Eleanor: What? What evidence do you have?')
    typewriter_print('You: You have the right to remain silent.')
    typewriter_print('You: Anything you say can and will be used against you in court.')
    state.refresh_screen()
    typewriter_print('She does not say anything further.')
    typewriter_print('A sheet of darkness casts over her face.')
    typewriter_print('You cuff her and lead her outside, where 3 police cars are parked.')
    typewriter_print('You hand her over to the chief deputy, who takes her back to the precinct.')
    state.current_objective='Wake up.'
    state.refresh_screen()
    typewriter_print('*BEEP BEEP BEEP*')
    time.sleep(1)
    typewriter_print('Your phone vibrates vigorously at 4am the next morning.')
    typewriter_print('It is the chief deputy.')
    typewriter_print('You pick up the phone, half asleep.')
    state.current_objective='Pick up the phone.'
    state.refresh_screen()
    typewriter_print(f'Chief: Detective {state.name}, I have great news.')
    typewriter_print(f'Chief: {character} has confessed to the murder of Thomas Vance.')
    typewriter_print('Chief: Good work, detective.')
    time.sleep(1)
    print("\033[H\033[J", end="")
    typewriter_print('Congratulations! You have successfully found the killer.')
    typewriter_print('Thank you for playing our game, and we hope you enjoyed it.')
    typewriter_print('If you would like to replay the game, press R.')
    typewriter_print('If you would like to quit, press Q')
    while True:
        ans = input().strip().lower()
        if ans == 'r':
            #restart
            pass
        elif ans == 'q':
            return