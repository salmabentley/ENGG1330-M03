# AI Use
Generative AI used: Yes

## Entry 1
- Member and date: Salma (2026/10/17)
- Tool and model/version: Gemini 3
- Purpose: to generate the beginning storylines for story purposes.
- Substantial parts affected (files/materials): main.py
- What was kept, changed, or rejected, and how results were checked (tests or 
corrections): Only used for story purposes, so only the name was changed and some story elements that needed more specifications



## Entry 2
- Member and date: Salma (2026/10/18)
- Tool and model/version: Gemini 3
- Purpose: to clear the terminal
- Substantial parts affected (files/materials): main.py
- What was kept, changed, or rejected, and how results were checked (tests or 
corrections): Gemini suggested printing print("\033[H\033[J", end=""). This was used to clear the terminal when needed.



## Entry 3
- Member and date: Han (2026/10/24)
- Tool and model/version: Gemini 3
- Purpose: to generate story’s details 
- Substantial parts affected (files/materials): computer.py, email.txt
- What was kept, changed, or rejected, and how results were checked (tests or 
corrections): The storyline is still the same. Material only used for story elements that needed more specifications and details.





## Entry 4
- Member and date: Han (2026/10/24)
- Tool and model/version: Gemini 3
- Purpose: to generate story’s details 
- Substantial parts affected (files/materials): computer.py, zip.txt
- What was kept, changed, or rejected, and how results were checked (tests or 
corrections): The storyline is still the same. Material only used for story elements that needed more specifications and details.



## Entry 5
- Member and date: Salma (2026/10/25)
- Tool and model/version: Gemini 3
- Purpose: to refine a loop within the play_safe function
- Substantial parts affected (files/materials): safe.py
- What was kept, changed, or rejected, and how results were checked (tests or 
corrections): Gemini suggested using a while True loop to create the game loop for the safe. The loop logic was used both in play_safe and in a separate function to infinitely loop through the yes or no options with error checking. Only the loop logic was taken from AI, the rest of the structure was hand coded.




## Entry 6
- Member and date: Salma (2026/10/25)
- Tool and model/version: Gemini 3
- Purpose: to create a script which allows md files to be rendered within the terminal constraints with styles
- Substantial parts affected (files/materials): txt.py
- What was kept, changed, or rejected, and how results were checked (tests or 
corrections): Majority of the code provided by Gemini was retained. It was tested by running a sample md file through the function. Some alterations needed to be made to the styling


## Entry 7
- Member and date: Salma (2026/10/28)
- Tool and model/version: Gemini 3
- Purpose: generate backstory for the plot
- Substantial parts affected (files/materials): safe.py
- What was kept, changed, or rejected, and how results were checked (tests or 
corrections): Some small details of the document were changed (like setting, which was incorrect), but was largely kept



## Entry 8
- Member and date: Salma (2026/10/28)
- Tool and model/version: Gemini 3
- Purpose: to allow arguments to be passed to md files for dynamic rendering
- Substantial parts affected (files/materials): md.py
- What was kept, changed, or rejected, and how results were checked (tests or 
corrections): only a few lines were changed. Display_md now accepts kwargs, and formats them within the md file



## Entry 9
- Member and date: Matthew (2026/11/05)
- Tool and model/version: Gemini 3
- Purpose: to create the format of the game overview
- Substantial parts affected (files/materials): documentation
- What was kept, changed, or rejected, and how results were checked (tests or 
corrections): only generate the format of the game overview and the content is done by ourselves



## Entry 10
- Member and date: Han (2026/11/7)
- Tool and model/version: Copilot
- Purpose: to create a table content for game rules
- Substantial parts affected (files/materials): README.md
- What was kept, changed, or rejected, and how results were checked (tests or 
corrections): the structure for game rules suggested by gemini is good but I also added more sub headings to the game rule that are relevant to the game like the movement input, suspect profiles and energy systems.



## Entry 11
- Member and date: Salma (2026/11/7)
- Tool and model/version: Gemini
- Purpose: to create a sticky hud for the game
- Substantial parts affected (files/materials): state.py
- What was kept, changed, or rejected, and how results were checked (tests or 
corrections): gemini suggested to create a universal screen renderer. The HUD code was taken from gemini and used in refresh_screen to update global variables like objective, time and energy.


## Entry 12
- Member and date: Salma (2026/11/8)
- Tool and model/version: Gemini
- Purpose: to allow for keyboard polling for continuous wasd input during the maze section
- Substantial parts affected (files/materials): maze.py
- What was kept, changed, or rejected, and how results were checked (tests or 
corrections): gemini first suggested to use the keyboard package, which was implemented at first. However, after running it within the docker container, I encountered some issues with keyboard not being allowed on linux machines. Therefore, I asked gemini to generate a general keyboard polling function to read keys. This is used in the final code.



## Entry 13
- Member and date: Salma (2026/11/10)
- Tool and model/version: Gemini
- Purpose: to create a resize function for the terminal
- Substantial parts affected (files/materials): state.py
- What was kept, changed, or rejected, and how results were checked (tests or 
corrections): gemini created a function that reads the terminal size then adds a message to resize the terminal if smaller than 80x24. I call the function every time refresh_screen is run



## Entry 14
- Member and date: Salma (2026/11/10)
- Tool and model/version: Gemini
- Purpose: to create a pause and restart function for the game
- Substantial parts affected (files/materials): state.py
- What was kept, changed, or rejected, and how results were checked (tests or 
corrections): I had already coded the pause function, but needed some help to pause the game timer as we have a running background timer. Gemini suggested just calculating the paused time and subtracting it off the total. This logic is used in the final code.


