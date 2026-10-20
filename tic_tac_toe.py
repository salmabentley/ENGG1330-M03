from tkinter import *
import random

def next_turn(row, column):
    global player
    if buttons[row][column]["text"] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]["text"] = player
            if check_winner() is False:
                player = players[1]
                label.config(text = (players[1] + "'s turn"))

def check_winner():
    pass

def empty_spaces():
    pass

def new_game():
    pass

window = Tk()
window.title("Tic-Tac-Toe")
players = ["X", "O"] 
player = random.choice(players)

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label (text=player + "'s turn", font = ("consolas", 40))
label.pack(side = "top")

reset_button = Button (text = "restart", font = ("consolas", 20), command = new_game)
reset_button.pack(side = "top")

frame = Frame(window)
frame.pack()

for row in range (3):
    for column in range (3):
        buttons[row][column] = Button(frame, text = "", font = ("consolas", 40), width = 5, height = 2,
                                      command = lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)



window.mainloop()

