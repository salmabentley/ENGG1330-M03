import state
from state import typewriter_print
import time
from termcolor import colored
import os
import sys

def accusation():
    state.current_objective='Arrest someone.'
    state.refresh_screen()
    typewriter_print('The rain outside begins pouring harder.', 0.05)
    typewriter_print('Faint sounds of thunder can be heard in the distance.', 0.05)
    typewriter_print('The old floors of the mansion reverbrate with each strike of lightning.', 0.05)
    typewriter_print('You enter the ballroom.', 0.05)
    state.refresh_screen()
    typewriter_print('Quiet individual whispers bounce against the walls.', 0.05)
    typewriter_print('It fills the room with anticipation.', 0.05)
    typewriter_print('The police have arrived outside the mansion.', 0.05)
    typewriter_print('It is time to put someone in handcuffs.', 0.05)
    state.refresh_screen()
    while True:
        typewriter_print('Who do you think killed Thomas Vance? This decision cannot be changed.')
        #player can only accuse who they have already talked to shown by the state.eleanor. If they have not talked to the character, it will show uncontacted
        print(f'(1) {'Eleanor Lan' if state.eleanor else colored('??? [Uncontacted]')} \n(2) {'George Tam' if state.george else colored('??? [Uncontacted]')} \n(3) {'Peter Lang' if state.peter else colored('??? [Uncontacted]')} \n(4) {'Gabrielle Ian' if state.gabrielle else colored('??? [Uncontacted]')}')
        ans=input()
        if ans=='1':
            #if the user has not talked to this character but accuse him/her, the function will loop again in the while True and they can't accuse this character
            if not state.eleanor:
                state.refresh_screen()
                typewriter_print('You have yet to unlock this character.')
            else:
                play_accusation('Eleanor Lan')
        if ans=='2':
            if not state.george:
                state.refresh_screen()
                typewriter_print('You have yet to unlock this character.')
            else:
                #if they already talked to the character then they would enter the play_accusation function
                play_accusation('George Tam')
        if ans=='3':
            if not state.peter:
                state.refresh_screen()
                typewriter_print('You have yet to unlock this character.')
            else:
                play_accusation('Peter Lang')
        if ans=='4':
            if not state.gabrielle:
                state.refresh_screen()
                typewriter_print('You have yet to unlock this character.')
            else:
                play_accusation('Gabrielle Ian')

def play_accusation(character):
    state.current_objective=f'Arrest {character}'
    state.refresh_screen()
    typewriter_print(f'You find {character} in the crowd.', 0.05)
    #different accusation will result in different dialogues
    if character=='Gabrielle Ian':
        typewriter_print('She is still holding the cigarette she was smoking earlier.', 0.05)
        typewriter_print('You approach her, gun holstered and handcuffs visible.', 0.05)
        typewriter_print('A hint of fear flashes in her eyes.', 0.05)
    elif character=='George Tam':
        typewriter_print('He is in the same place as when you first met him.', 0.05)
        typewriter_print('You approach him, gun holstered and handcuffs visible.', 0.05)
        typewriter_print('He looks confused, almost bewildered.', 0.05)
    elif character=='Peter Lang':
        typewriter_print('He seems to have helped himself to another glass of whiskey.', 0.05)
        typewriter_print('You approach him, gun holstered and handcuffs visible.', 0.05)
        typewriter_print('He does not seem to notice, staring off into the distance instead.', 0.05)
    else:
        typewriter_print('She is on her phone, seemingly texting someone.', 0.05)
        typewriter_print('You approach her, gun holstered and handcuffs visible.', 0.05)
        typewriter_print('She looks up from her phone, in shock to see you.', 0.05)

    state.refresh_screen()
    typewriter_print(f'You: {character}, you are under arrest under suspicion for the murder of Thomas Vance.', 0.05)
    typewriter_print(f'{character}: What? What evidence do you have?', 0.05)
    typewriter_print('You: You have the right to remain silent.', 0.05)
    typewriter_print('You: Anything you say can and will be used against you in court.', 0.05)
    state.refresh_screen()
    if character == 'Eleanor Lan':
        typewriter_print('She does not say anything further.', 0.05)
        typewriter_print('A sheet of darkness casts over her face.', 0.05)
    elif character == 'Gabrielle Ian':
        typewriter_print('Gabrielle: This is ridiculous.', 0.05)
        typewriter_print('Gabrielle: While you\'re wasting your time with me, the actual killer is still out there!', 0.05)
        typewriter_print('She begins swearing profusely, hurling insults at you.', 0.05)
    elif character == 'Peter Lang':
        typewriter_print('He goes completely silent and expressionless.', 0.05)
        typewriter_print('The strong smell of whiskey lingers in the air as you cuff him.', 0.05)
    else:
        typewriter_print('George: How can this be...', 0.05)
        typewriter_print('George: Did Eleanor frame me?', 0.05)
        typewriter_print('A look of despair casts over his face.', 0.05)
    time.sleep(1)
    if character == 'Eleanor Lan' or character == 'Gabrielle Ian':
        typewriter_print('You cuff her and lead her outside, where 3 police cars are parked.', 0.05)
        typewriter_print('You hand her over to the chief deputy, who takes her back to the precinct.', 0.05)
    else:
        typewriter_print('You cuff him and lead him outside, where 3 police cars are parked.', 0.05)
        typewriter_print('You hand him over to the chief deputy, who takes him back to the precinct.', 0.05)
    state.current_objective='Wake up.'
    time.sleep(1)
    state.refresh_screen()
    typewriter_print('*BEEP BEEP BEEP*', 0.1)
    time.sleep(1)
    typewriter_print('Your phone vibrates vigorously at 4am the next morning.', 0.05)
    typewriter_print('It is the chief deputy.', 0.05)
    typewriter_print('You pick up the phone, half asleep.', 0.05)
    state.current_objective='Pick up the phone.'
    state.refresh_screen()

    #if the user correctly identifies the murderer
    if character == 'Eleanor Lan':
        typewriter_print(f'Chief: Detective {state.name}, I have great news.', 0.05)
        typewriter_print(f'Chief: {character} has confessed to the murder of Thomas Vance.', 0.05)
        typewriter_print('Chief: If you didn\'t know, Vance paid her off in court.', 0.05)
        typewriter_print('Chief: She has been planning her revenge since then.', 0.05)
        typewriter_print('Chief: Good work, detective.', 0.05)
    else:
        typewriter_print(f'Chief: Detective {state.name}, I have news.', 0.05)
        typewriter_print(f'Chief: {character} did not kill Vance.', 0.05)
        typewriter_print('Chief: It was Eleanor Lan.', 0.05)
        state.refresh_screen()
        typewriter_print('Chief: If you didn\'t know, Vance paid her off in court.', 0.05)
        typewriter_print('Chief: She has been planning her revenge since then.', 0.05)
        typewriter_print('Chief: Unfortunately, since you arrested the wrong person, she has fled the country.', 0.05)
        state.refresh_screen()
        typewriter_print('Chief: This will be going on your record, detective.', 0.05)
    time.sleep(1)
    print("\033[H\033[J", end="")

    if character == 'Eleanor Lan':
        typewriter_print('Congratulations! You have successfully found the killer.')
    else:
        typewriter_print('Oh no! You failed to catch the killer. Maybe next time?')
    typewriter_print('Thank you for playing our game, and we hope you enjoyed it.')
    typewriter_print('If you would like to replay the game, enter R.')
    typewriter_print('If you would like to quit, enter Q')
    #while loop ensures that incorrect format answer will be reprompted
    while True:
        ans = input().strip().lower()
        if ans == 'r':
            #restart
            os.execv(sys.executable, [sys.executable] + sys.argv)

        elif ans == 'q':
            sys.exit()
