from state import typewriter_print
import state
import time

def george():
    state.refresh_screen()
    typewriter_print('You re-enter the grand ballroom where everyone stands anxiously.')
    typewriter_print('You see the man who was crouched next to Thomas Vance, but you can\'t quite put a finger on who he is.')
    typewriter_print('You go up to him and strike up a conversation')
    state.refresh_screen()
    typewriter_print('[New objective] Interrogate the mystery person of interest.')
    state.current_objective='Interrogate the mystery person of interest.'
    time.sleep(1)
    state.refresh_screen()
    typewriter_print('You: Hi, just wanted to ask you a few questions about your recent whereabouts if that\'s okay with you.')
    typewriter_print('???: Sure, may I ask why?')
    typewriter_print('You: Just want to cover all bases, that\'s all.')
    while True:
        typewriter_print("(1) Who are you? \n(2) Sorry, I have some place else to be ")
        number = input()
        if number == '1':
            state.refresh_screen()
            typewriter_print("You: May I know who you are?", delay=0.05)
            typewriter_print("George: I am George Tam, I work in Vance Construction with Thomas Vance, I'm his assistant.", delay=0.05)
            state.current_objective='Interrogate George Tam'
            state.george=True
            typewriter_print("You: Why are you here tonight?", delay=0.05)
            typewriter_print("George: I always stay with my boss when he needs to go to events, just to ensure nothing goes wrong.", delay=0.05)
            state.refresh_screen()
            typewriter_print("You: So why were you in the office with Thomas when he passed?", delay=0.05)
            typewriter_print("George: I wasn't, I was asked by Madame Lan to bring her some food from the kitchen" , delay=0.05)
            while True:
                typewriter_print("(1) What then? \n(2) What did you see when you were walking to the kitchen? \n(3) Thank you for your time. ")
                number_1 = input()
                state.refresh_screen()
                if number_1 == '1':
                    typewriter_print("You: What then?" , delay=0.05)
                    typewriter_print("George: When I went back to the ballroom, everyone was gone, so I went to the office and saw my boss was lying on the floor, then I screamed so loudly. It was so terrifying!!!" , delay=0.05)
                elif number_1 == '2':
                    typewriter_print("You: What did you see when you were walking to the kitchen?" , delay=0.05)
                    typewriter_print("George: I didn't see anything, but when I was walking back to the ballroom, I passed through the office and I saw the door was open a bit, but I didn't open it as I thought my boss was finding something, and I didn't want to bother him" , delay=0.05)
                    typewriter_print("You: What if you were actually the one who got in the office and killed Thomas Vance?" , delay=0.05)
                    typewriter_print("George: Of course not! You can ask Eleanor Lan whether I have brought her some food! Go ask for her!" , delay=0.05)    
                    typewriter_print("[Unlocked new dialogue option] Eleanor Lan" , delay=0.05)    
                    state.eleanor_food=True
                elif number_1 == '3':
                    return
                elif number_1 == 'h' or number_1 == 'q':
                    state.check_player_input(number_1)
                else:
                    typewriter_print ("Energy level: -1", 0.05) #Energy goes down by 1 everytime users input wrong command
                    typewriter_print ("Reason: Please input your answer as required", 0.05)
                    state.energy-=1
                    state.refresh_screen()
        elif number == '2':
            return
        elif number == 'h' or number == 'q':
            state.check_player_input(number)
        else:
            typewriter_print ("Energy level: -1", 0.05) #Energy goes down by 1 everytime users input wrong command
            typewriter_print ("Reason: Please input your answer as required", 0.05)
            state.energy-=1
            state.refresh_screen()
    