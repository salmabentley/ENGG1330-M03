from state import typewriter_print
import sys
import time
import state

def gabrielle():
    state.refresh_screen()
    typewriter_print("You go to the end of the hallway.", delay=0.05)
    typewriter_print("A young woman smokes by the window.", delay=0.05)
    typewriter_print("Name: Gabrielle Ian", 0.05)
    # typewriter_print("Relationship: Thomas Vance's ex-girlfriend", 0.05)
    state.current_objective='Interrogate Gabrielle'
    state.gabrielle=True
    state.refresh_screen()

    typewriter_print ("[New objective] Interrogate Gabrielle", delay=0.05)
    typewriter_print ("Gabrielle: Hi detective, what are you doing here this late? Still investigating huh?", delay=0.05)
    # typewriter_print("You:", delay=0.05)

    while True:
        print ("(1) Yes, I'm investigating the murder of Mr.Vance\n(2) No, I'm just walking around, for a quick break you know...\n(3) None of your business")
        q0 = input("").strip()
        state.refresh_screen()
        if q0 == "3":
            typewriter_print ("Gabrielle: ...",0.05)
            typewriter_print ("Gabrielle: Good to know. And please, get out of here, you disrespectful bastard!", 0.05)
            state.refresh_screen()
            typewriter_print ("Gabrielle strongly pushes you back. She goes straight to the bathroom locks the door.", 0.05)
            typewriter_print ("Energy level: -5", 0.05) #Energy goes down by 5
            typewriter_print ("Reason: Disrespecting NPCs", 0.05)
            typewriter_print ("[Game update] You can no longer interct with Gabrielle.")
            state.energy-=5
            state.gabrielle_disabled=True
            return #Player goes back to the map and continues investigating other NPCs
        elif q0 == "2":
            typewriter_print("Gabrielle: Oh I see, I see. How is the investigation going?", 0.05)
            typewriter_print ("You: So far not very well, I'm still lacking a lot of information.", 0.05)
            typewriter_print ("You: It'd be great if you could answer a few questions for me.", 0.05)
            typewriter_print("Gabrielle: Go ahead, detective", 0.05)
            break
        elif q0 == "1":
            typewriter_print("Gabrielle: How is everything so far?", 0.05)
            typewriter_print("Gabrielle: If you figure out who killed him, please let me know cause I'd have to thank them for this!", 0.05)
            typewriter_print("You: Haha. Would you mind if I ask you a few question about today's dinner?", 0.05)
            typewriter_print("Gabrielle: Go ahead, detective", 0.05)
            break
        elif q0 == 'h' or q0 == 'q':
            state.check_player_input(q0)
        else:
            typewriter_print ("Energy level: -1", 0.05) #Energy goes down by 1]] everytime users input wrong command
            typewriter_print ("Reason: Please input your answer as required", 0.05)
            state.energy-=1
            state.refresh_screen()


    state.refresh_screen()


    while True:
        typewriter_print("You:", 0.05)
        print ("(1) What were you doing at 9pm today?\n(2) Would you mind telling me about your relationship with Mr.Vance?\n(3) How were you invited to this dinner?")
        q1 = input("").strip()
        state.refresh_screen()
        if q1 == "1":
            typewriter_print("Gabrielle: I was taking a shower, it's been a long day", 0.05)
            while True:
                print ("(1) Do you have any evidence to prove that?\n(2) Good enough, thank you so much for sharing.")
                q1_1 = input("").strip()
                state.refresh_screen()

                if q1_1 == "1":
                    typewriter_print("Gabrielle: Evidence? I need to prove that I\'m showering now? How ridiculous.", 0.05)
                    typewriter_print('You: I just want to cover all bases ma\'am. Is there anyone that can vouch for you?')
                    typewriter_print('Gabrielle: Vouch for me? Do you think I killed Thomas? You\'re crazy.')
                    time.sleep(0.5)
                    state.refresh_screen()
                    typewriter_print("Gabrielle strongly pushes you back. She puts out her cigarette and walks away.", 0.05)
                    typewriter_print('[Game Update] You can no longer interact with Ms. Gabrielle.')
                    state.gabrielle_disabled=True
                    return
                elif q1_1 == "2":
                    typewriter_print ("Gabrielle: Great, hope you got all you needed.", 0.05)
                    state.refresh_screen()
                    time.sleep(0.5)
                    typewriter_print ("Gabrielle continues smoking at the window.", 0.05)
                    return
                elif q1_1 == 'h' or q1_1 == 'q':
                    state.check_player_input(q1_1)
                else:
                    typewriter_print ("Energy level: -1", 0.05) #Energy goes down by 2 everytime users input wrong command
                    typewriter_print ("Reason: Please input your answer as required", 0.05)
                    state.energy-=1
                    state.refresh_screen()
        elif q1 == "2":
            state.refresh_screen()
            typewriter_print("Gabrielle: Thomas is my ex.", 0.05)
            typewriter_print("Gabrielle: That bastard BETRAYED me!", 0.05)
            typewriter_print("Gabrielle: I am glad he is dead now.", 0.05)
            while True:
                print ("(1) Then why did you attend this party?\n(2) Do you mind sharing your story about your relationship?\n(3) I think I have enough information.")
                q1_2 = input().strip()
                state.refresh_screen()
                if q1_2 == "1":
                    typewriter_print("Gabrielle: Just for fun.", 0.05)
                    typewriter_print("Gabrielle: Sometimes it's refreshing to remind yourself of those who have betrayed you", 0.05)
                    typewriter_print ("You: I see, thank you for your information.", 0.05)
                    state.refresh_screen()
                    time.sleep(0.5)
                    typewriter_print ("Gabrielle continues smoking at the window, her puffs bigger than the last.", 0.05)
                    return
                elif q1_2 == "2":
                    typewriter_print ("Gabrielle: I do, in fact.", 0.05)
                    typewriter_print ("Gabrielle: Why would anyone want to recall such a low point in their life?", 0.05)
                    typewriter_print ("Gabrielle: I\'ll be happy to answer any other question.", 0.05)
                elif q1_2 == "3":
                    typewriter_print ("Gabrielle: Great, I hope your investigation goes well.", 0.05)
                    return
                elif q1_2 == 'h' or q1_2 == 'q':
                    state.check_player_input(q1_2)
                else:
                    typewriter_print ("Energy level: -1", 0.05) #Energy goes down by 2 everytime users input wrong command
                    typewriter_print ("Reason: Please input your answer as required", 0.05)
                    state.energy-=1
                    state.refresh_screen()
        elif q1 == "3":
            state.refresh_screen()
            typewriter_print ("Gabrielle: He didn’t invite me, I come as I please.", 0.05)
            typewriter_print ("Gabrielle: I know his home better than himself!", 0.05)
            while True:
                print ("(1) What do you think of his death?\n(2) Okay, thank you for sharing.")
                q1_3 = input().strip().lower()
                state.refresh_screen()
                if q1_3 == "1":
                    typewriter_print("Gabrielle: Satisfied, finally somebody killed that cheating bastard.", 0.05)
                    typewriter_print("Gabrielle: If it wasn\'t for the legal consequences, I would've done it myself ages ago!", 0.05)
                    typewriter_print("You: Ms. Gabrielle, are you confessing to conspiracy to murder?", 0.05)
                    typewriter_print("Gabrielle: Don\'t be silly. Who wouldn\'t wish death on their cheating ex?", 0.05)
                    state.refresh_screen()
                    typewriter_print('You: I\'ll let you off this once Ms. Gabrielle.')
                    typewriter_print('You: But just know that everything you say to me can be used against you in the investigation.')
                    typewriter_print('Gabrielle: Whatever.')
                    return
                elif q1_3 == "2":
                    typewriter_print ("Gabrielle: Of course.", 0.05)
                    time.sleep(0.5)
                    typewriter_print ("Gabrielle continues smoking at the window, her puffs bigger than the last.", 0.05)
                    return
                else:
                    typewriter_print ("Energy level: -1", 0.05) #Energy goes down by 2 everytime users input wrong command
                    typewriter_print ("Reason: Please input your answer as required", 0.05)
                    state.energy-=1
                    state.refresh_screen()
        elif q1 == 'h' or q1 == 'q':
            state.check_player_input(q1)
        else:
            typewriter_print ("Energy level: -1", 0.05) #Energy goes down by 2 everytime users input wrong command
            typewriter_print ("Reason: Please input your answer as required", 0.05)
            state.energy-=1
            state.refresh_screen()