import time
import random

def print_board(board):
    print()
    for i in range(0, 9, 3):
        row = board[i:i+3]
        print (" "+" | ".join(row))
        if i < 6:
            print ("-----------")
    print()

def check_winner(board, player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
        ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in wins)

def is_full(board):
    return " " not in board

def computer_move(board):
    empty_boxes = [i for i,c in enumerate(board) if c == " "]
    if empty_boxes:
        choice = random.choice(empty_boxes)
        return choice

def play():
    board = [" "] * 9
    time.sleep(1)
    print (input("Complete the challenge to unlock the computer. Press Enter to continue."))
    time.sleep(1)
    print ("You are X. The computer is O. Squares are numbered 1-9, left to right, top to bottom.")
    time.sleep(2)
    print_board([str(i+1) if c == " " else c for i, c in enumerate(board)])
    time.sleep(1)
    print ("The game starts now. You go first, good luck!")

    while True:
        move = None
        while move is None:
            raw = input ("Enter your move (1-9): ").strip()
            if raw.isdigit() and 1 <= int(raw) <= 9 and board[int(raw)-1] == " ":
                move = int(raw) - 1
            else:
                print ("Invalid move. Try again.\n")
                time.sleep(1)
        board[move] = "X"


        if check_winner(board, "X"):
            print_board(board)
            print ("You win!")
            break
        if is_full(board):
            print_board(board)
            print ("It's a tie!")
            break

        computer_choice = computer_move(board)
        board[computer_choice] = "O"
        print_board(board)

        if check_winner(board, "O"):
            print ("Computer wins!")
            break
        
        if is_full(board):
            print ("It's a tie!")
            break


if __name__ == "__main__":
    play()
