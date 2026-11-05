from introduction import typewriter_print
import state
state.refresh_screen()
#if choosing_number == 4:
#    typewriter_print("Who are you? (1) , Where were you when Thomas Vance was killed? (2) , What's the relationship between you and Thomas Vance? (3)" , delay=0.05)
#else:
while True:
    typewriter_print("Who are you? (1) , Where were you when Thomas Vance was killed? (2) ,quit(3)" , delay=0.05)
    number = int(input())
    if number == 1:
        state.refresh_screen()
        typewriter_print("Who are you?", delay=0.05)
        typewriter_print("Character: I am Peter Lang")
        typewriter_print("How do you know Thomas Vance?", delay=0.05)
        typewriter_print("Character: I first met him at college, and sometimes I really miss the memories there...")
    if number == 2:
        state.refresh_screen()
        typewriter_print("Where were you are when Thomas Vance was killed?" , delay = 0.05)
        typewriter_print("Character: I was in the toilet, but I don't know where the office is." , delay = 0.05)
        while True:
            typewriter_print("Did you pass by the office? (1) , quit (2)" , delay = 0.05)
            number_2 = int(input())
            if number_2 == 1:
                state.refresh_screen()
                typewriter_print("Character: I don't even know where is the office! How do I know whether I have passed through it?" , delay = 0.05)
                typewriter_print("But if you went to the toilet, you need to pass through the office, are you lying !?" , delay = 0.05)
                typewriter_print('Character: NO!' , delay = 0.05)
            else:
                break
    #if number == 3:
        #state.refresh_screen()
        #typewriter_print("What's the relationship between you and Thomas Vance?" , delay = 0.05)
        #typewriter_print("Character: I was his best friend. He was the most successful person that I have ever met in my life, as he founded his own company by himself and earned a lot of money. Sometimes I get jealous why he's so successful, but I'm still happy for him" , delay = 0.05)
    if number == 3:
        break