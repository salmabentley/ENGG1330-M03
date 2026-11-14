import time
from room1.introduction import get_name, play_intro
from room1.safe import play_safe, safe_contents
from room1.computer import explore_computer, unlock_computer
from room1.body import dead_body
import state
from state import typewriter_print 
from room1.md import display_md

from room2.maze import draw_maze, move

investigated_all=False        #detects whether player has explored all rooms for the first time to play special dialogue

if __name__ == "__main__":
    # play intro
    get_name()
    play_intro()

    # game loop
    state.start=time.time()
    while True:

        state.current_objective = 'Investigate the room' #to let the player to explore room 2 (the maze) after they have investigated all the rooms in room 1 (the office)
        state.refresh_screen()
        if state.safe_investigated and state.computer_investigated and state.body_investigated:
            if not investigated_all:
                typewriter_print('You have investigated all parts of the room.')
                typewriter_print('You have now unlocked the rest of the mansion.')
                typewriter_print('You are free to continue exploring the Office, but note that time is ticking.')
                state.refresh_screen()
                investigated_all=True
            print('(1) Investigate body  \n(2) Go to computer  \n(3) Go to the safe \n(4) Explore the mansion ')
        else:
            print('(1) Investigate body  \n(2) Go to computer  \n(3) Go to the safe')

        choice = input()
        if choice =='1': #let the player choose which part of the room they want to investigate, and if they have already investigated that part of the room, they can choose to investigate it again 
            state.current_objective = 'Investigate the body'
            dead_body()
            state.body_investigated=True
        elif choice == '2':
            state.current_objective = 'Investigate the computer'
            if not state.computer_unlocked:
                state.computer_unlocked = unlock_computer()
            else:
                explore_computer()
            state.computer_investigated=True
        elif choice =='3':
            state.current_objective = 'Investigate the safe'
            if not state.safe_unlocked:
                state.safe_unlocked=play_safe()
            else:
                safe_contents()
            state.safe_investigated=True
        state.check_player_input(choice)

        if state.safe_investigated and state.computer_investigated and state.body_investigated and choice == '4':
            #room2
            state.refresh_screen()
            typewriter_print('Are you sure you would like to explore the mansion now?') #final confirm to the player if they wnat to explore room 2, because once they enter the mansion, they cannot go back to the office
            typewriter_print('You will not be able to return to this room.')
            while True:
                typewriter_print('Explore mansion (Y) Continue exploring the office (N)')
                ans=input().strip().lower()
                state.check_player_input(ans)

                if ans == 'y':
                    #room2
                    # This guarantees energy starts at 100, decreases smoothly with time, and can NEVER go below 0
                    state.elapsed = time.time() - state.start - state.paused_time  # lock in final elapsed time
                    state.energy = round(max(0.0, 100.0 - (state.elapsed / 600.0) * 100.0),0)
                    state.current_room=2
                    state.refresh_screen()
                    typewriter_print('You push open the heavy mahogany door once more.')
                    typewriter_print('It feels much heavier than the first time.')
                    typewriter_print('You walk out the door toward the grand hallway.')
                    state.refresh_screen()
                    typewriter_print('You look back at the clock in the office.')
                    typewriter_print('Time has passed significantly.')
                    typewriter_print('You start to feel the fatigue from investigating.')
                    typewriter_print('But you have no time to lose.')
                    time.sleep(1)
                    state.refresh_screen()
                    typewriter_print('[New objective] Explore the mansion.')
                    state.current_objective='Explore the mansion'
                    draw_maze()
                    move()
                    pass
                else:
                    break
