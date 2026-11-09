from ..state import typewriter_print
from .. import state
import sys
import time

def eleanor():
    state.refresh_screen()
    typewriter_print("You walk to the conference room and knock on the door.", delay=0.05)
    typewriter_print("You hear a voice from inside the room say, 'Come in.'", delay=0.05)
    typewriter_print("You slowly open the door and see a woman who is reading on a sofa.", delay=0.05)
    typewriter_print("Name: Eleanor Lan", 0.05)
    # typewriter_print("Relationship: Thomas Vance's employee's wife", 0.05)
    state.current_objective='Interrogate Eleanor'
    state.refresh_screen()
    typewriter_print ("[New Goal] Interrogate Eleanor", delay=0.05)
    typewriter_print ("Eleanor: Hi detective, why are you here this late?", delay=0.05)
    typewriter_print("You: I'm still investigating Mr.Vance's case at the moment and I need to gather your alibi.", delay=0.05)
    typewriter_print("Eleanor: Sure, go ahead", 0.05)
    while True:
        print ("(1) What were you doing at 9pm today?\n(2) What's your relationship with Mr.Vance?\n(3) How did you get invited to this party?")
        q1 = input("You: ").strip()
        state.refresh_screen()

        if q1 == "1":
            typewriter_print("Eleanor: I just stayed in this room, calling my husband and my daughter for nearly the whole night!", 0.05)
            typewriter_print("You: Oh really?", 0.05)
            while True:
                print("(1) Why was your husband not invited to Mr.Vance's dinner?\n(2) Do you have any evidence to prove that?\n(3) Thank you so much for your information, I would get back to you later.")
                q1_1 = input("You: ").strip()
                state.refresh_screen()
                if q1_1 == "1":
                    typewriter_print("Eleanor: We both got invited to Mr.Vance's dinner, but today he is taking our daughter to Disneyland so it’s only me here.", 0.05)
                    typewriter_print("You: I see, I see. What do you think of Mr.Vance's death?", 0.05)
                    typewriter_print ("Eleanor: Terrified actually, I have never imagined that I would become a witness of a deadly case.", 0.05)
                    typewriter_print("You: I get it, this is a terrible experience...", 0.05)
                    typewriter_print ("You: Anyway, thank you so much for your information. Now just take a good night rest!")
                    typewriter_print ("Eleanor: Great, see you tomorrow", 0.05)
                    state.refresh_screen()
                    typewriter_print ("You leave the room and continue walking around the building...", 0.05)
                    return
                elif q1_1 == "2":
                    typewriter_print ("Eleanor: What do you mean? Didn’t I just tell you that I called my husband and my daughter for the whole night? Go and talk to other people, I have nothing to say anymore!", 0.05)
                    print()
                    time.sleep(0.5)
                    typewriter_print ("Eleanor stands up and leaves the room.", 0.05)
                    return
                elif q1_1 == "3":
                    typewriter_print ("Eleanor: Great, see you tomorrow", 0.05)
                    print()
                    time.sleep(0.5)
                    typewriter_print ("You leave the room and continue walking around the building...", 0.05)
                    return
                else:
                    typewriter_print ("Energy level: -2", 0.05) #Energy goes down by 2 everytime users input wrong command
                    typewriter_print ("Reason: Please input your answer as required", 0.05)
                    state.energy-=2
                    state.refresh_screen()
        elif q1 == "2":
            state.refresh_screen()
            typewriter_print("Eleanor: My husband is a senior worker under Thomas Vance so we often get invited to attend his dinner and gatherings.", 0.05)
            while True:
                typewriter_print("You:", 0.05)
                print ("(1) Why was he not here? \n(2) What do you think about Thomas Vance's death?\n(3) Thank you so much, goodnight and see you tomorrow")
                q1_2 = input("You: ").strip()
                state.refresh_screen()
                if q1_2 == "1":
                    typewriter_print("Eleanor: Normally, my husband will come with me but today he is taking our daughter to Disneyland so it’s only me here", 0.05)
                    typewriter_print ("You: I see, I see. Anyway, thank you so much for your information!", 0.05)
                    typewriter_print ("Eleanor: My pleasure, I hope that helps. See you tomorrow.", 0.05)
                    print()
                    time.sleep(0.5)
                    typewriter_print ("You leave the room and continue walking around the building...", 0.05)
                    return    
                elif q1_2 == "2":
                    typewriter_print ("Eleanor: Terrified actually, I have never imagined that I would become a witness of a deadly case.", 0.05)
                    typewriter_print ("You: Right, witnessing a deadly case is a terrible experience. Are you feeling okay?", 0.05)
                    typewriter_print("Eleanor: Yeah, I'm fine. I feel a lot better after calling my husband and daughter!", 0.05)
                    typewriter_print("You: That's good to hear. Thank you so much for your information, I'd get back to you later. Now just take a good night rest!", 0.05)
                    print()
                    time.sleep(0.5)
                    typewriter_print ("You leave the room and continue walking around the building...", 0.05)
                    return
                elif q1_3 == "3":
                    typewriter_print ("Eleanor: Great, see you tomorrow", 0.05)
                    print()
                    time.sleep(0.5)
                    typewriter_print ("You leave the room and continue walking around the building...", 0.05)
                    return
                else:
                    typewriter_print ("Energy level: -2", 0.05) #Energy goes down by 2 everytime users input wrong command
                    typewriter_print ("Reason: Please input your answer as required", 0.05)
                    state.energy-=2
                    state.refresh_screen()  
        elif q1 == "3":
            state.refresh_screen()
            typewriter_print("Eleanor: My husband is a senior worker under Thomas Vance so we often get invited by him for dinner and gatherings.", 0.05)
            typewriter_print("You:", 0.05)
            print ("(1) Why was not he here?\n(2) What do you think of his death?\n(3) Okay, thank you so much for sharing and see you tomorrow")
            q1_3 = input("You: ").strip()
            state.refresh_screen()
            if q1_3 == "1":
                typewriter_print("Eleanor: Normally, my husband will come with me but today he is taking our daughter to Disneyland so it’s only me here.", 0.05)
                typewriter_print ("You: I see, I see. Anyway, thank you so much for your information!", 0.05)
                typewriter_print ("Eleanor: My pleasure, I hope that helps. See you tomorrow.", 0.05)
                print()
                time.sleep(0.5)
                typewriter_print ("You leave the room and continue walking around the building...", 0.05)
                return    
            elif q1_3 == "2":
                typewriter_print ("Eleanor: Terrified actually, I have never imagined that I would become a witness of a deadly case.", 0.05)
                typewriter_print ("You: Right, witnessing a deadly case is a terrible experience. Are you feeling okay?", 0.05)
                typewriter_print("Eleanor: Yeah, I'm fine. I feel a lot better after calling my husband and daughter!", 0.05)
                typewriter_print("You: That's good to hear. Thank you so much for your information, I'd get back to you later. Now just take a good night rest!", 0.05)
                print()
                time.sleep(0.5)
                typewriter_print ("You leave the room and continue walking around the building...", 0.05)
                return
            elif q1_3 == "3":
                typewriter_print ("Eleanor: Great, see you tomorrow.", 0.05)
                print()
                time.sleep(0.5)
                typewriter_print ("You leave the room and continue walking around the building...", 0.05)
                return
            else:
                typewriter_print ("Energy level: -2", 0.05) #Energy goes down by 2 everytime users input wrong command
                typewriter_print ("Reason: Please input your answer as required", 0.05)
                state.energy-=2
                state.refresh_screen()
        else:
                typewriter_print ("Energy level: -2", 0.05) #Energy goes down by 2 everytime users input wrong command
                typewriter_print ("Reason: Please input your answer as required", 0.05)
                state.energy-=2
                state.refresh_screen()
        return