from ..state import typewriter_print
import sys
import time

def gabrielle():
    print("\033[H\033[J", end="")
    typewriter_print("You walk straight up, approaching a young woman who is smoking by the window.", delay=0.05)
    typewriter_print("Name: Gabrielle Iang", 0.05)
    typewriter_print("Relationship: Thomas Vance's ex-girlfriend", 0.05)
    print("\033[H\033[J", end="")

    typewriter_print ("[New Goal] Interrogate Garbrielle", delay=0.05)
    typewriter_print ("Gabrielle: Oh greetings our beloved detective, what are you doing here at this late! Still investigating huh?", delay=0.05)
    typewriter_print("You:", delay=0.05)

    while True:
        print ("(1) Yes, I'm investigating the murder of Mr.Vance\n(2) No, I'm just walking around, for a quick break you know...\n(3) None of your business")
        q0 = input("You: ").strip()
        print("\033[H\033[J", end="")
        if q0 == "3":
            typewriter_print ("Gabrielle:...",0.05)
            typewriter_print ("Gabrielle: Good to know. And please, get out of here, you disrespectful bastard!", 0.05)
            print("\033[H\033[J", end="")
            typewriter_print ("Gabrielle strongly pushes you back. She goes straight to her room and locks the door.", 0.05)
            typewriter_print ("Energy level: -5", 0.05) #Energy goes down by 5
            typewriter_print ("Reason: Disrespecting NPCs", 0.05)
            sys.exit() #Player goes back to the map and continues investigating other NPCs
        elif q0 == "2":
            typewriter_print("Gabrielle: Oh I see, I see. How is the investigation going?", 0.05)
            typewriter_print ("You: So far not that well, I'm still lacking a lot of information. It'd be my pleasure if you're willing to help me with this", 0.05)
            typewriter_print("Gabrielle: Go ahead my detective", 0.05)
            break
        elif q0 == "1":
            typewriter_print("Gabrielle: How is everything so far? If you figure out who killed him, please let me know cause I'd have to thank them for this!", 0.05)
            typewriter_print("You: Yes, I would definitely let you know once I figure out everything. Would you mind if I ask you a few question about today's dinner?", 0.05)
            typewriter_print("Gabrielle: Go ahead my detective", 0.05)
            break
        else:
            typewriter_print ("Energy level: -2", 0.05) #Energy goes down by 2 everytime users input wrong command
            typewriter_print ("Reason: Please input your answer as required", 0.05)
            print("\033[H\033[J", end="")


    print("\033[H\033[J", end="")


    while True:
        typewriter_print("You:", 0.05)
        print ("(1) What did you do at 9pm today?\n(2) Would you mind telling me about your relationship with Mr.Vance?\n(3) Why did you attend the dinner?")
        q1 = input("You: ").strip()
        print("\033[H\033[J", end="")
        if q1 == "1":
            typewriter_print("Gabrielle: Just getting a shower you know, it's been a long day", 0.05)
            while True:
                typewriter_print("You:", 0.05)
                print ("(1) Do you have any evidence to prove that?\n(2) Do you mind sharing your story about you two relationship?\n(3) Good enough, thank you so much for sharing and see you tomorrow")
                q1_1 = input("You: ").strip()
                print("\033[H\033[J", end="")

                if q1_1 == "1":
                    typewriter_print("Gabrielle: What do you mean?!? I truly don't understand where this conversation is going. See you tomorrow!", 0.05)
                    print()
                    time.sleep(0.5)
                    typewriter_print ("Gabrielle strongly pushes you back. She goes straight to her room and locks the door.", 0.05)
                    sys.exit()
                elif q1_1 == "2":
                    typewriter_print ("Gabrielle: No! What do you want me to tell?! How did I get betrayed by him or what!", 0.05)
                    typewriter_print ("Why would you even want somebody to recall that part of their lives. I am too tired right now, see you tomorrow", 0.05)
                    print()
                    time.sleep(0.5)
                    typewriter_print ("Gabrielle strongly pushes you back. She goes straight to her room and locks the door.", 0.05)
                    sys.exit()
                elif q1_1 == "3":
                    typewriter_print ("Gabrielle: Great, see you tomorrow", 0.05)
                    print()
                    time.sleep(0.5)
                    typewriter_print ("Gabrielle walks back to her room and you continues walking around the building...", 0.05)
                    sys.exit()
                else:
                    typewriter_print ("Energy level: -2", 0.05) #Energy goes down by 2 everytime users input wrong command
                    typewriter_print ("Reason: Please input your answer as required", 0.05)
                    print("\033[H\033[J", end="")
        elif q1 == "2":
            print("\033[H\033[J", end="")
            typewriter_print("Gabrielle: That bastard BETRAYED me! And I am glad that he is dead now", 0.05)
            while True:
                typewriter_print("You:")
                print ("(1) Then why did you attend the dinner, didn't he invite you?\n(2) Do you mind sharing your story about you two relationship?\n(3) Thank you so much, goodnight and see you tomorrow")
                q1_2 = input("You: ").strip()
                print("\033[H\033[J", end="")
                if q1_2 == "1":
                    typewriter_print ("Gabrielle: He didn’t invite me, I just came as I wanted to. I know his home better than I know myself!", 0.05)
                    typewriter_print ("You: I see, thank you so much for your information! Good night and see you tomorrow.", 0.05)
                    typewriter_print ("Gabrielle: Great, see you tomorrow", 0.05)
                    print()
                    time.sleep(0.5)
                    typewriter_print ("Gabrielle walks back to her room and you continues walking around the building...", 0.05)
                    sys.exit()
                elif q1_2 == "2":
                    typewriter_print ("Gabrielle: No! What do you want me to tell?! How did I get betrayed by him or what!", 0.05)
                    typewriter_print ("Why would you even want somebody to recall that part of their lives. I am too tired right now, see you tomorrow", 0.05)
                    print()
                    time.sleep(0.5)
                    typewriter_print ("Gabrielle strongly pushes you back. She goes straight to her room and locks the door.", 0.05)
                    sys.exit()
                elif q1_2 == "3":
                    typewriter_print ("Gabrielle: Great, see you tomorrow", 0.05)
                    print()
                    time.sleep(0.5)
                    typewriter_print ("Gabrielle walks back to her room and you continues walking around the building...", 0.05)
                    sys.exit()
                else:
                    typewriter_print ("Energy level: -2", 0.05) #Energy goes down by 2 everytime users input wrong command
                    typewriter_print ("Reason: Please input your answer as required", 0.05)
                    print("\033[H\033[J", end="")
        elif q1 == "3":
            print("\033[H\033[J", end="")
            typewriter_print("Gabrielle: Just for fun, sometimes it's good to remind yourself of who has betrayed you", 0.05)
            while True:
                typewriter_print("You:", 0.05)
                print ("(1) What do you think of his death?\n(2) Okay, thank you so much for sharing and see you tomorrow")
                q1_3 = input("You: ").strip()
                print("\033[H\033[J", end="")
                if q1_3 == "1":
                    typewriter_print("Gabrielle: Satisfied, finally somebody killed him for me or else, I will be the one who kill him first!", 0.05)
                    typewriter_print("But wait a minute, are you suspecting me?! How dare you, get out of my room now!", 0.05)
                    print()
                    time.sleep(0.5)
                    typewriter_print ("Gabrielle strongly pushes you back. She goes straight to her room and locks the door.", 0.05)
                    sys.exit()
                elif q1_3 == "2":
                    typewriter_print ("Gabrielle: Great, see you tomorrow", 0.05)
                    print()
                    time.sleep(0.5)
                    typewriter_print ("Gabrielle walks back to her room and you continues walking around the building...", 0.05)
                    sys.exit()
                else:
                    typewriter_print ("Energy level: -2", 0.05) #Energy goes down by 2 everytime users input wrong command
                    typewriter_print ("Reason: Please input your answer as required", 0.05)
                    print("\033[H\033[J", end="")
        else:
                typewriter_print ("Energy level: -2", 0.05) #Energy goes down by 2 everytime users input wrong command
                typewriter_print ("Reason: Please input your answer as required", 0.05)
                print("\033[H\033[J", end="")