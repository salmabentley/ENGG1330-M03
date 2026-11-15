import time
import random
import state

def print_board(board):    
    #print the board 
    print()
    #the loop runs 3 times, 0,3,6 each represents one row of the tic tac toe board
    for i in range(0, 9, 3):   
        #one row is a slicing of the board list      
        row = board[i:i+3] 
        #the row is joined by the bar | between each character and a leading space between the first character for indentation and alignment     
        print (" "+(" | ".join(row)))     
        if i < 6:
             #print the grid divider between rows but only after the first two rows with i=0,3
            print ("-----------")      
    print()

def check_winner(board, player):
    #list all posible winning position at the board index. each tuple is the index of the board to win the game so if at index 0,1,2 of the board are the same then this counts as a win
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
        ]       
    #loop through every element inside every tuple in the wins list. if the board at that specific index all equal to each other "X" or "O" then it is a win.
    #any() function checks all the winning lines and return true if it finds at least one winning line where the player/computer has three in a row
    return any(board[a] == board[b] == board[c] == player for a, b, c in wins)      


def is_full(board):
    #check whether the board is full or not, if it is full then the game is tie     
    return " " not in board     

def computer_move(board):
    #loop over the free boxes in the board, all the free boxes are put into the list so that the computer has a list of empty boxes to 'play'
    empty_boxes = [i for i,c in enumerate(board) if c == " "]       
    if empty_boxes:
        #computer will randomly choose one box in the list     
        choice = random.choice(empty_boxes)     
        #return the computer's choice as an integer indicating the box chosen
        return choice       

def play():
    #create the board with 9 empty spaces in one list for 3x3 grid
    board = [" "] * 9       
    time.sleep(1)
    print ("You are X. The computer is O. Squares are numbered 1-9, left to right, top to bottom.")
    time.sleep(2)
    #loops through every spaces in the board with index, replaces the empty string with str(i+1) or else keeps existing character. this create a list of what to display on the grid when passing to the print_board function
    print_board([str(i+1) if c == " " else c for i, c in enumerate(board)]) 
    time.sleep(1)
    #the while loop ensures that the player and computer will compete until there is a winner or the game is a tie
    while True:     
        #condition to start a loop until the player makes their move
        move = None     
        while move is None:
            raw = input ("Enter your move (1-9): ").strip()
            #check the player's user: digit from 1-9, and the box must be empty
            if raw.isdigit() and 1 <= int(raw) <= 9 and board[int(raw)-1] == " ":   
                #as the board uses zero-index so we need to minus 1 to convert back to 0-index; move is no longer None so break out of the loop
                move = int(raw) - 1    
            #if player needs help or pause
            elif raw.isalpha():
                state.check_player_input(raw)       
            else:
                #move is still None so the loop starts over
                print ("Invalid move. Try again.\n")        
                time.sleep(1)
        #the position at index move will be updated to "X"
        board[move] = "X"       

        #after player turn, the program checks whether this move creates any winner or not or tie
        if check_winner(board, "X"):       
            print_board(board)
            #if after the player input meets the winning condition, then play() will return True and end the function
            return True     
        #if this is a tie, also end the function by return False
        if is_full(board):      
            print_board(board)
            return False
        
        #if neither player wins or ties, then the computer will take it move by using the computer_move function, return a digit/index
        computer_choice = computer_move(board)
        #this will fill in the box with O as played by the computer      
        board[computer_choice] = "O"        
        print_board(board)      

        #after the computer choice, the program checks the condition for winning and ties, if not another round starts
        if check_winner(board, "O"):        
            return False
        
        #if " " not in the board so all the position is filled and no winning condition has been met through the above testing then it is a tie
        if is_full(board):     
            return False, "It's a tie!"
            


if __name__ == "__main__":
    play()
