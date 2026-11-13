# AI Use
Generative AI used: Yes

## Entry 1
- Member and date: Salma (2026/10/17)
- Tool and model/version: Gemini 3
- Purpose: to generate the beginning storylines for story purposes.
- Substantial parts affected (files/materials): main.py
- What was kept, changed, or rejected, and how results were checked (tests or 
corrections): Only used for story purposes, so only the name was changed and some story elements that needed more specifications

Query: here is the backstory for my game. Can you help me generate a news article on the death of the employee and its legal proceedings?

detective invited to an event by an ex client. The ex client is murdered in a room, 3-5 people were seen going inside the room. Construction company due to negligence resulted in the death of an employee, company got out of it due to better resources, wife plans for revenge



## Entry 2
- Member and date: Salma (2026/10/18)
- Tool and model/version: Gemini 3
- Purpose: to clear the terminal
- Substantial parts affected (files/materials): main.py
- What was kept, changed, or rejected, and how results were checked (tests or 
corrections): Gemini suggested printing print("\033[H\033[J", end=""). This was used to clear the terminal when needed.

Query: I want to build a typewriter function that clears the terminal after a set number of lines. Is there a function that allows me to do that?



## Entry 3
- Member and date: Han (2026/10/24)
- Tool and model/version: Gemini 3
- Purpose: to generate story’s details 
- Substantial parts affected (files/materials): computer.py, email.txt
- What was kept, changed, or rejected, and how results were checked (tests or 
corrections): The storyline is still the same. Material only used for story elements that needed more specifications and details.

Query: I am a secretary for Mr. Vance, George Tam, and he is CEO of Vance Construction company. I want to write an email to him reminding him about next Monday's 10am morning meetings with the Construction Department




## Entry 4
- Member and date: Han (2026/10/24)
- Tool and model/version: Gemini 3
- Purpose: to generate story’s details 
- Substantial parts affected (files/materials): computer.py, zip.txt
- What was kept, changed, or rejected, and how results were checked (tests or 
corrections): The storyline is still the same. Material only used for story elements that needed more specifications and details.

Query: here is the back story of my game:
detective invited to an event by an ex client. The ex-client was murdered in a room, 3-5 people were seen going inside the room. Construction company due to negligence resulted in the death of an employee, the company got out of it due to better resources. Help me generate a proof of negligence documents of this construction company with the following details:
CEO: Thomas Vance
Company: Vance Construction
Dead employee: Arthur Lan




## Entry 5
- Member and date: Salma (2026/10/25)
- Tool and model/version: Gemini 3
- Purpose: to refine a loop within the play_safe function
- Substantial parts affected (files/materials): safe.py
- What was kept, changed, or rejected, and how results were checked (tests or 
corrections): Gemini suggested using a while True loop to create the game loop for the safe. The loop logic was used both in play_safe and in a separate function to infinitely loop through the yes or no options with error checking. Only the loop logic was taken from AI, the rest of the structure was hand coded.

Query: 
def play_safe():
    print("\033[H\033[J", end="")
    time.sleep(1)
    typewriter_print('You approach the safe, its red light blinking ominously.', delay=0.05)
    typewriter_print('Above the safe, you see a poster showing all the blood types.', delay=0.05)
    typewriter_print('Looking down, you see a keypad with numbers 0-9, with 3 small letters under each number', delay=0.05)
    typewriter_print('Would you like to enter a code? Yes (y) No (n)', delay=0.05)
    res=input()
    if (res=='n'):
        return False
    elif (res=='y'):
        print("\033[H\033[J", end="")
        print('\nKeypad:\n')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('~~ 1(-) ~~ 2(ABC) ~~ 3(DEF) ~~')
        print('~ 4(GHI) ~~ 5(JKL) ~~ 6(MNO) ~')
        print('~ 7(PQRS) ~ 8(TUV) ~ 9(WXYZ) ~')
        print('~~~~ * ~~~~~ 0(+) ~~~~~ # ~~~~')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        code=input('Enter the code:  ')
        if (code!='2220'):
            typewriter_print('The safe beeps angrily, rejecting your code.', delay=0.05)
            typewriter_print('Would you like to re-enter another code? Yes (y) No (n)', delay=0.05)

i want this code to loop back to where the elif starts. i feel like i should use separate functions and invoke it circularly





## Entry 6
- Member and date: Salma (2026/10/25)
- Tool and model/version: Gemini 3
- Purpose: to create a script which allows md files to be rendered within the terminal constraints with styles
- Substantial parts affected (files/materials): txt.py
- What was kept, changed, or rejected, and how results were checked (tests or 
corrections): Majority of the code provided by Gemini was retained. It was tested by running a sample md file through the function. Some alterations needed to be made to the styling

Query: is there a way to render md files in the terminal with styling? since there is a 80-column by 24-row terminal area restriction, I want the md files preferably to be separated per restriction with a next/previous page function



## Entry 7
- Member and date: Salma (2026/10/28)
- Tool and model/version: Gemini 3
- Purpose: generate backstory for the plot
- Substantial parts affected (files/materials): safe.py
- What was kept, changed, or rejected, and how results were checked (tests or 
corrections): Some small details of the document were changed (like setting, which was incorrect), but was largely kept

Query: can you help me generate a police style investigation document on the following details?
detective investigates vance construction on grounds of corporate negligence, leading to the death of arthur lan
Investigation made my third party regulation company found that there were cost cutting on load bearing beams
Vance construction claimed the beams were outsourced to a material company owned by Gabrielle ######
Eleanor Lan (wife of Arthur Lan), pressed charges on grounds of negligence and corruption
After a 3 month trial, charges were dropped against Vance Construction by the victim
please also include the characters George Tam (assistant to Thomas Vance, CEO of Vance construction) and Peter Lang (best friend of Thomas Vance but is jealous of his wealth) 




## Entry 8
- Member and date: Salma (2026/10/28)
- Tool and model/version: Gemini 3
- Purpose: to allow arguments to be passed to md files for dynamic rendering
- Substantial parts affected (files/materials): md.py
- What was kept, changed, or rejected, and how results were checked (tests or 
corrections): only a few lines were changed. Display_md now accepts kwargs, and formats them within the md file

Query: is there any way to do dynamic md files? i want to put the user inputted name in the md file





## Entry 9
- Member and date: Salma (2026/11/05)
- Tool and model/version: Gemini 3
- Purpose: to create the format of the game overview
- Substantial parts affected (files/materials): documentation
- What was kept, changed, or rejected, and how results were checked (tests or 
corrections): only generate the format of the game overview and the content is done by ourselves

Query: give me an example of the format of a game overview



## Entry 10
- Member and date: Han (2026/11/7)
- Tool and model/version: Copilot
- Purpose: to create a table content for game rules
- Substantial parts affected (files/materials): README.md
- What was kept, changed, or rejected, and how results were checked (tests or 
corrections): the structure for game rules suggested by gemini is good but I also added more sub headings to the game rule that are relevant to the game like the movement input, suspect profiles and energy systems.

Query: Im writing a game rulebook for a game that I code in python. what is a good structure look like




