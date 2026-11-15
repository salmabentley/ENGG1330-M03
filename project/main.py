import time
from room1.introduction import get_name, play_intro
from room1.safe import play_safe, safe_contents
from room1.computer import explore_computer, unlock_computer
from room1.body import dead_body
import state
from state import typewriter_print 
from room2.maze import draw_maze, move

investigated_all=False        #detects whether player has explored all rooms for the first time to play special dialogue

if __name__ == "__main__":
    # checks that the terminal size is within the 80x24 limit
    state.check_terminal_size()
    # play intro
    get_name()
    play_intro()

    # game loop
    state.start=time.time()     # gets the time when the player starts room 1
    while True:

        state.current_objective = 'Investigate the room'
        state.refresh_screen()

        #if all rooms have been interacted with, allow player to move to room 2
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
        if choice =='1':
            state.current_objective = 'Investigate the body'
            dead_body()
            state.body_investigated=True
        elif choice == '2':
            state.current_objective = 'Investigate the computer'

            #allows players to bypass the unlock if they already unlocked the computer previously
            if not state.computer_unlocked:
                state.computer_unlocked = unlock_computer()
            else:
                explore_computer()
            state.computer_investigated=True
        elif choice =='3':
            state.current_objective = 'Investigate the safe'

            #allows player to bypass the safe lock if the player already unlocked the safe
            if not state.safe_unlocked:
                state.safe_unlocked=play_safe()
            else:
                safe_contents()
            state.safe_investigated=True

        #always checks if the player presses h or q
        state.check_player_input(choice)

        # checks if all parts of the room have been investigated AND player wants to enter room 2
        if state.safe_investigated and state.computer_investigated and state.body_investigated and choice == '4':
            #room2
            state.refresh_screen()
            typewriter_print('Are you sure you would like to explore the mansion now?')
            typewriter_print('You will not be able to return to this room.')

            # allow players to confirm their choice
            while True:
                typewriter_print('Explore mansion (Y) Continue exploring the office (N)')
                ans=input().strip().lower()
                state.check_player_input(ans)

                # proceed to room 2
                if ans == 'y':
                    
                    # calculate energy by calculating the percentage of time left over in room 1
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

    #                 # render the mansion and allow players to move
                    draw_maze()
                    move()
                    pass
                else:
                    # return player to room 1 
                    break
