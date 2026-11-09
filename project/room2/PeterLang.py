from ..state import typewriter_print
from .. import state

def peter():
    state.refresh_screen()
    typewriter_print('You enter the kitchen and see a man crouched over the counter')
    typewriter_print('He slowly sips from his glass of Jim Beam Whiskey')
    if state.photo:
        typewriter_print('You recognise him as the man in the photo with Thomas Vance')
        typewriter_print('Peter Lang', delay=0.1)
    typewriter_print('You approach him to ask a few questions')
    if state.photo:
        typewriter_print('[New objective] Interrogate Peter Lang')
        state.current_objective='Interrogate Peter Lang'
    else:
        typewriter_print('[New objective] Interrogate the man')
        state.current_objective='Interrogate the man'
    state.refresh_screen()
    typewriter_print(f'You: Hello, I am detective {state.name}, do you mind answering a few of my questions?')
    if state.photo:
        typewriter_print('Peter: Of course, fire away.')
    else:
        typewriter_print('???: Of course, fire away.')
    while True:
        if state.photo:
            typewriter_print("(1) Who are you? \n(2) Where were you when Thomas Vance was killed? \n(3) What’s the relationship between you and Thomas Vance? \n(4) Sorry, I have somewhere else to be ")
        else:
            typewriter_print("(1) Who are you? \n(2) Where were you when Thomas Vance was killed? \n(4) Sorry, I have somewhere else to be ")
        number = input()
        if number == '1':
            state.current_objective='Interrogate Peter Lang'
            state.refresh_screen()
            typewriter_print("You: May I know your name?", delay=0.05)
            typewriter_print("Peter: I am Peter Lang")
            typewriter_print("You: How do you know Thomas Vance?", delay=0.05)
            typewriter_print("Peter: I first met him at college, and sometimes I really miss the memories there...")
        elif number == '2' :
            state.refresh_screen()
            typewriter_print("You: Where were you are when Thomas Vance was killed?" , delay = 0.05)
            typewriter_print("Peter: I was in the toilet when I first heard the scream." , delay = 0.05)
            while True:
                typewriter_print("(1) Did you pass by the office?  \n(2)Thank you for your cooperation. ")
                number_2 = input()
                if number_2 == '1':
                    state.refresh_screen()
                    typewriter_print("Peter: What office? How do I know whether I have passed through it?t" , delay = 0.05)
                    typewriter_print("Peter: I\'ve never been here before, it\'s my first time being invited." , delay = 0.05)
                    typewriter_print("You: But if you went to the toilet, you have to pass through the office. Are you lying?" , delay = 0.05)
                    typewriter_print('Peter: NO!' , delay = 0.05)
                else:
                    return
        elif number=='3':
            #if player found the photo in room one, this dialogue will be unlocked
            if state.photo:
                state.refresh_screen()
                typewriter_print('You: What\'s the relationship between you and Thomas?', delay = 0.05) 
                typewriter_print('Peter: He\'s just a family friend, I don\'t know him that well.', delay = 0.05)
                state.refresh_screen()
                typewriter_print('You know this isn\'t true.', delay = 0.05)
                typewriter_print('Distant family friends don\'t usually have a space in each other\'s wallets.', delay = 0.05)
                typewriter_print('You take the photo out and place it on the counter.', delay = 0.05)
                state.refresh_screen()
                typewriter_print('You: Are you sure about that?', delay = 0.05)
                typewriter_print('Peter sighs heavily, a gloomy look casts over his face.', delay = 0.05)
                typewriter_print('He downs the rest of his liquor in one go.', delay = 0.05)
                state.refresh_screen()
                typewriter_print('Peter: I was his best friend.', delay = 0.05)
                typewriter_print('Peter: He was the most successful person that I have ever met in my life', delay = 0.05)
                typewriter_print('Peter: He founded his own company by himself and earned a lot of money.', delay = 0.05)
                typewriter_print('Peter: Sometimes I get jealous why he’s so successful, but I\'m still happy for him', delay = 0.05)
            