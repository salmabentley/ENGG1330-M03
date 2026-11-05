from introduction import typewriter_print
import state
state.refresh_screen()
while True:
    typewriter_print("Who are you? (1) , Why don't you follow your boss to the office where he got killed? (2) , quit (3)" , delay = 0.05)
    number_ = int(input())
    if number_ == 1:
        state.refresh_screen()
        typewriter_print("Who are you?", delay=0.05)
        typewriter_print("Character: I am George Tam, I work in Vance Construction with Thomas Vance, I'm his assistant.", delay=0.05)
        typewriter_print("Why are you coming to the event tonight?", delay=0.05)
        typewriter_print("Character: I always stay with my boss when he needs to go to the events, to ensure nothing goes wrong.", delay=0.05)
    if number_ == 2:
        state.refresh_screen()
        typewriter_print("Why don't you follow your boss to the office where he got killed?", delay=0.05)
        typewriter_print("Character: Because I was assigned by Madam Lan to bring her some food in the kitchen" , delay=0.05)
        while True:
            typewriter_print("What then? (1) , What did you see when you were walking to the kitchen? (2) , quit (3)" , delay=0.05)
            number_1 = int(input())
            state.refresh_screen()
            if number_1 == 1:
                typewriter_print("What then?" , delay=0.05)
                typewriter_print("Character: When I went back to the ballroom, everyone was gone, so I went to the office and saw my boss was lying on the floor, then I screamed so loudly. It was so terrifying!!!" , delay=0.05)
            if number_1 == 2:
                typewriter_print("What did you see when you were walking to the kitchen?" , delay=0.05)
                typewriter_print("Character: I didn't see anything, but when I was walking back to the ballroom, I passed through the office and I saw the door was open a bit, but I didn't open it as I thought my boss was finding something and I'm not going to bother him" , delay=0.05)
                typewriter_print("Are you lying that you were actually the one who got in the office and killed Thomas Vance?" , delay=0.05)
                typewriter_print("Character: Of course not! You can ask Eleanor Lan whether I have brought her some food! Go ask for her!" , delay=0.05)    
            if number_1 == 3:
                break
    if number_ == 3:
        break
    