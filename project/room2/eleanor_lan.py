from state import typewriter_print
import state
import time

def eleanor():
    state.refresh_screen()
    typewriter_print("You walk to the conference room and knock on the door.", delay=0.05)
    typewriter_print("You hear a voice from inside the room say, 'Come in.'", delay=0.05)
    typewriter_print("You slowly open the door and see a woman on a sofa.", delay=0.05)
    typewriter_print("Name: Eleanor Lan", 0.05)
    typewriter_print("Relationship: Thomas Vance's employee's wife", 0.05)
    state.current_objective='Interrogate Eleanor'
    state.eleanor=True
    state.refresh_screen()
    typewriter_print ("[New Goal] Interrogate Eleanor", delay=0.05)
    typewriter_print ("Eleanor: Hi detective, why are you still here so late?", delay=0.05)
    typewriter_print("You: I'm still investigating Mr. Vance's case at the moment and I need to gather your alibi.", delay=0.05)
    typewriter_print("Eleanor: Sure, go ahead", 0.05)
    while True:
        # print ("(1) What were you doing at 9pm today?\n(2) What's your relationship with Mr.Vance?\n(3) How did you get invited to this party?")
        if state.money_found:
            print ("(1) What did you do at 9pm today?\n(3) Why did you attend this dinner?\n(2) Why does Mr. Vance have money for you?")
        else:
            print ("(1) What did you do at 9pm today?\n(2) Why did you attend this dinner?")
        q1 = input().strip()
        state.refresh_screen()

        if q1 == "1":
            typewriter_print("Eleanor: I was in this room, calling my husband and my daughter for basically the whole night!", 0.05)
            typewriter_print("You: Oh really?", 0.05)
            while True:
                if state.eleanor_food:
                    print("(1) Why wasn\'t your husband invited to Mr.Vance's dinner?\n(2) Do you have any evidence to prove that?\n(3) George said you asked him to bring you food. \n(4) Thank you for your information.")
                else:
                    print("(1) Why wasn\'t your husband invited to Mr.Vance's dinner?\n(2) Do you have any evidence to prove that?\n(3) Thank you for your information.")

                q1_1 = input("").strip()
                state.refresh_screen()
                if q1_1 == "1":
                    typewriter_print("Eleanor: We both got invited to Mr.Vance's dinner, but today he is taking our daughter to Disneyland so it’s just me here.", 0.05)
                    typewriter_print("You: I see, I see. What do you think of Mr.Vance's death?", 0.05)
                    typewriter_print ("Eleanor: Terrified actually, I have never imagined that I would become a witness in a deadly case.", 0.05)
                    typewriter_print("You: I get it, this is a terrible experience...", 0.05)
                    typewriter_print ("You: Anyway, thank you so much for your information. Now just take a good night rest!")
                    # typewriter_print ("Eleanor: Great, see you tomorrow", 0.05)
                    state.refresh_screen()
                    typewriter_print ("You leave the room and continue walking around the building...", 0.05)
                    return
                elif q1_1 == "2":
                    typewriter_print ("Eleanor: What do you mean? Didn’t I just tell you that I called my husband and my daughter for the whole night?", 0.05)
                    typewriter_print('Eleanor: Are you suspecting me of killing Mr. Vance??')
                    typewriter_print('You: Just covering all bases ma\'am.')
                    typewriter_print('Eleanor: Ridiculous. Go and talk to other people, I have nothing to say anymore!')
                    state.refresh_screen()
                    time.sleep(0.5)
                    typewriter_print ("Eleanor stands up and leaves the room.", 0.05)
                    typewriter_print ("[Game update] You can no longer talk to Eleanor Lan", 0.05)
                    state.eleanor_disabled=True
                    return
                elif q1_1 == "3" and not state.eleanor_food:
                    return
                elif q1_1 == '3' and state.eleanor_food:
                    typewriter_print('Eleanor: What? I never told him to bring me food.')
                    typewriter_print('Eleanor: He said he wanted to go to the office with his boss!')
                    state.refresh_screen()
                    typewriter_print('You ask George to drop by the conference room to explain his side.')
                    typewriter_print('George: What??? You are lying! You are trying to plant evidence on me!')
                    typewriter_print('George: Are you trying to cover up the fact that you killed him?')
                    typewriter_print('Eleanor: Ridiculous! Why would I do such a thing?')
                    state.refresh_screen()
                    typewriter_print('Things begin to get physical.')
                    typewriter_print('You come between them to put an end to the fight before it starts.')
                    typewriter_print('You ask George to leave.')
                    typewriter_print('You apologise to Eleanor and leave the room to give her some space.')
                    state.eleanor_disabled=True
                    typewriter_print('[Game update] You can no longer talk to Eleanor Lan')
                    return
                elif q1_1 == 'h' or q1_1 == 'q':
                    state.check_player_input(q1_1)
                else:
                    typewriter_print ("Energy level: -1", 0.05) #Energy goes down by 1 everytime users input wrong command
                    typewriter_print ("Reason: Please input your answer as required", 0.05)
                    state.energy-=1
                    state.refresh_screen()
        elif q1 == "2":
            state.refresh_screen()
            typewriter_print("Eleanor: My husband is a senior worker under Thomas Vance so we often get invited by him for dinner and gatherings.", 0.05)
            typewriter_print("You:", 0.05)
            print ("(1) Why was he not here?\n(2) What do you think of his death?\n(3) Okay, thank you so much for sharing")
            q1_3 = input().strip()
            state.refresh_screen()
            if q1_3 == "1":
                typewriter_print("Eleanor: Normally, my husband will come with me but today he is taking our daughter to Disneyland", 0.05)
                typewriter_print ("You: I see, I see. Anyways, thank you so much for your information!", 0.05)
                typewriter_print ("Eleanor: My pleasure, I hope that helps", 0.05)
                print()
                time.sleep(0.5)
                typewriter_print ("You leave the room and continue walking around the building...", 0.05)
                return    
            elif q1_3 == "2":
                typewriter_print ("Eleanor: Terrified actually, I have never imagined that I would become a witness of a deadly case.", 0.05)
                typewriter_print ("You: Right, witnessing a deadly case is a terrible experience. Are you feeling okay?", 0.05)
                typewriter_print("Eleanor: Yeah, I'm fine. I feel a lot better after calling my husband and daughter!", 0.05)
                typewriter_print("You: That's good to hear. Thank you so much for your information, I'd get back to you later. Now just take a good night rest!", 0.05)
                time.sleep(0.5)
                typewriter_print ("You leave the room and continue walking around the building...", 0.05)
                return
            elif q1_3 == "3":
                typewriter_print ("Eleanor: Great, see you!", 0.05)
                time.sleep(0.5)
                typewriter_print ("You leave the room and continue walking around the building...", 0.05)
                return
            elif q1_3 == 'h' or q1_3 == 'q':
                state.check_player_input(q1_3)
            else:
                typewriter_print ("Energy level: -1", 0.05) #Energy goes down by 1 everytime users input wrong command
                typewriter_print ("Reason: Please input your answer as required", 0.05)
                state.energy-=1
                state.refresh_screen()

        elif q1 == "3" and state.money_found:
            state.refresh_screen()
            typewriter_print('You place your phone on the table, showing her a picture of the safe contents.')
            typewriter_print("Eleanor doesn't seem to be too surprised by the photo")
            typewriter_print("Eleanor: It's a long story...")
            typewriter_print("Eleanor: Mr. Vance has been a nice guy, at least to me and to my husband.", 0.05)
            state.refresh_screen()
            typewriter_print('Eleanor: We usually get invited to his dinner parties.')
            typewriter_print('Eleanor: He would always discuss their construction projects while I chat with his now ex-wife.')
            typewriter_print('Eleanor: But it\'s been a while since the accident...')
            state.refresh_screen()
            typewriter_print("You: What accident?", 0.05)
            typewriter_print("Eleanor: My husband died from an accident while he was on site...", 0.05)
            typewriter_print ("You: I'm very sorry to hear that.")
            while True:
                print ("(1) How did Mr.Vance react then? \n(2) How did you get over it?\n(3) I apologize for bringing back old memories.")
                q1_2 = input().strip()
                print("\033[H\033[J", end="")
                if q1_2 == "1":
                    typewriter_print("Eleanor: He had supported me throughout the whole journey since Arthur's death!", 0.05)
                    typewriter_print("Eleanor: The money is to support me and my daughter.", 0.05)
                    typewriter_print("Eleanor: I can't imagine how my life would have turned out without him.", 0.05)
                    typewriter_print("You: I see, I see...", 0.05) 
                    state.refresh_screen()
                    typewriter_print("You: It's getting late. Thank you so much for your time.")
                    typewriter_print ("Eleanor: My pleasure, I hope that helps. See you tomorrow.", 0.05)
                    time.sleep(0.5)
                    typewriter_print ("You leave the room and continue walking around the building...", 0.05)
                    return
                elif q1_2 == "2":
                    typewriter_print ("Eleanor: It had been hard for me since then but Vance's company supported me along the way.", 0.05)
                    typewriter_print ("You: Oh really, that's nice to hear. I didn't know Vance is such a kind person.", 0.05)
                    typewriter_print("Eleanor: Yeah, he really is. I feel lucky getting to know him...", 0.05)
                    typewriter_print("You: Thank you so much for your information. Please have good night\'s rest!", 0.05)
                    time.sleep(0.5)
                    typewriter_print ("You leave the room and continue walking around the building...", 0.05)
                    return
                elif q1_2 == "3":
                    typewriter_print ("Eleanor: Don't worry, it's been more than a year now so I'm a lot better", 0.05)
                    typewriter_print("You: It's good to hear that! Thank you for your time.")
                    time.sleep(0.5)
                    typewriter_print ("You leave the room and continue walking around the building...", 0.05)
                elif q1_2 == 'h' or q1_2 == 'q':
                    state.check_player_input(q1_2)
                else:
                    typewriter_print ("Energy level: -1", 0.05) #Energy goes down by 1 everytime users input wrong command
                    typewriter_print ("Reason: Please input your answer as required", 0.05)
                    state.energy-=1
                    state.refresh_screen()
        elif q1 == 'h' or q1 == 'q':
            state.check_player_input(q1)
        else:
            typewriter_print ("Energy level: -1", 0.05) #Energy goes down by 1 everytime users input wrong command
            typewriter_print ("Reason: Please input your answer as required", 0.05)
            state.energy-=1
            state.refresh_screen()
            