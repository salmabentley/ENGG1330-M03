from state import typewriter_print
import state

def peter():
    state.refresh_screen()
    typewriter_print('You enter the kitchen and see a man crouched over the counter')
    typewriter_print('He slowly sips from his glass of Jim Beam Whiskey')

    #if the player found the photo in room 1, then they already know who peter is
    if state.photo_found:
        typewriter_print('You recognise him as the man in the photo with Thomas Vance')
        typewriter_print('Peter Lang', delay=0.1)
    typewriter_print('You approach him to ask a few questions')
    if state.photo_found:
        typewriter_print('[New objective] Interrogate Peter Lang')
        state.current_objective='Interrogate Peter Lang'
    else:
        typewriter_print('[New objective] Interrogate the man')
        state.current_objective='Interrogate the man'
    state.refresh_screen()
    typewriter_print(f'You: Hello, I am detective {state.name}, do you mind answering a few of my questions?')
    if state.photo_found:
        typewriter_print('Peter: Of course, fire away.')
    else:
        typewriter_print('???: Of course, fire away.')
    while True:
        #allow players to pick a secret dialogue options if they find the photo in room 1
        if state.photo_found:
            typewriter_print("(1) Who are you? \n(2) Where were you when Thomas Vance was killed? \n(3) What’s the relationship between you and Thomas Vance? \n(4) Sorry, I have somewhere else to be ")
        else:
            typewriter_print("(1) Who are you? \n(2) Where were you when Thomas Vance was killed? \n(3) Sorry, I have somewhere else to be ")
        choice_1 = input()
        if choice_1 == '1':
            #update state variables if players have not discovered peter yet
            state.current_objective='Interrogate Peter Lang'
            state.peter=True
            state.refresh_screen()
            typewriter_print("You: May I know your name?", delay=0.05)
            typewriter_print("Peter: I am Peter Lang")
            typewriter_print("You: How do you know Thomas Vance?", delay=0.05)
            typewriter_print("Peter: I first met him at college, and sometimes I really miss the memories there...")
        elif choice_1 == '2' :
            state.refresh_screen()
            typewriter_print("You: Where were you are when Thomas Vance was killed?" , delay = 0.05)
            typewriter_print("Peter: I was in the toilet when I first heard the scream." , delay = 0.05)
            while True:
                typewriter_print("(1) Did you pass by the office?  \n(2)Thank you for your cooperation. ")
                choice_2 = input()
                if choice_2 == '1':
                    state.refresh_screen()
                    typewriter_print("Peter: What office? How do I know whether I have passed through it?t" , delay = 0.05)
                    typewriter_print("Peter: I\'ve never been here before, it\'s my first time being invited." , delay = 0.05)
                    typewriter_print("You: But if you went to the toilet, you have to pass through the office. Are you lying?" , delay = 0.05)
                    typewriter_print('Peter: NO!' , delay = 0.05)
                elif choice_2 == 'h' or choice_2 == 'q':
                    state.check_player_input(choice_2)
                elif choice_2=='2':
                    return
                else:
                    typewriter_print ("Energy level: -1", 0.05) #Energy goes down by 1 everytime users input wrong command
                    typewriter_print ("Reason: Please input your answer as required", 0.05)
                    state.energy-=1
                    state.refresh_screen()
        elif choice_1=='3':
            #if player found the photo in room one, this dialogue will be unlocked
            if state.photo_found:
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
            else:
                #return player back to the maze if they havent unlocked the dialogue
                return
        elif choice_1 == 'h' or choice_1 == 'q':
            state.check_player_input(choice_1)
        elif choice_1 == '4' and state.photo_found:
            #return players back to the maze if players unlocked the secret dialogue and enter 4
            return
        else:
            typewriter_print ("Energy level: -1", 0.05) #Energy goes down by 1 everytime users input wrong command
            typewriter_print ("Reason: Please input your answer as required", 0.05)
            state.energy-=1
            state.refresh_screen()
            