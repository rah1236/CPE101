# Project 3 - Tic-Tac-Toe Simulator
#
# Name: Raheel Rehmatullah
# Instructor: S. Einakian
# Section: 7
# Functions definitions comes here

import random

# 1) welcome function
#Welcomes user into program
#none -> str
def welcome():
    print("Welcome to the world of Tic Tac Toe")
    print("Please use the following cell numbers make your move")
    userSelection = input("Do you want to play against a CPU(1) or a human(2)")
    print("Excellent, the board will be layed out like this:")
    print("""
   1 |  2  | 3
-----------------
   4 |  5  | 6
-----------------
   7 |  8  | 9

    """)
    return(userSelection)

# 2) create_board function
#creates board list
#none -> list
def create_board():
    return [" "," "," "," "," "," "," "," "," "]


# 3) print_board function
#Prints out board for user
#none -> none
def print_board(board):

        print("""
    -----------------
       {0} |  {1}  | {2}
    -----------------
       {3} |  {4}  | {5}
    -----------------
       {6} |  {7}  | {8}
    -----------------""".format(*board))

#print_board(["o","x","x","o","o","x","x","o","o"])

# 4) pick_letter functio
#Allows user to pick x or o
#none -> str
def pick_letter():
    userInput = input("X or O?").lower()
    if userInput != "x" and userInput != "o":
        print("That's not one of the options. Try again.")
        userInput = input("X or O?").lower()
    else:
        return(userInput)



# 5) get_input Function
#gets location of letter and inserts letter
#list, str -> list
def get_input(board, letter, opLetter):
    userInput = input("Where do you want to place your piece? (1-9)")
    inRange = False
    while(not inRange):
        for i in range(0,10):
            if int(userInput) == i:
                inRange = True
    while(board[int(userInput)-1] == opLetter or board[int(userInput)-1] == letter):
        print("Sorry, that spot is taken, please choose somewhere else.")
        userInput = input("Where do you want to place your piece? (1-9)")
    board[int(userInput)-1] = letter
    return(board)


# 6) check_rows function
#checks rows for winState
#list->bool
def check_rows(board):
    winningLetter = " "
    for i in range(0,7,3):
        if (board[i] == board[i+1] == board[i+2] != " "):
            winningLetter = board[i]
            return True, winningLetter
    return False, " "

# 7) check_cols function
#checks columbs for winState
#list->bool
def check_cols(board):
    winningLetter = " "
    for i in range(0,3,1):
        if (board[i] == board[i+3] == board[i+6] != " "):
            winningLetter = board[i]
            return True, winningLetter
    return False, " "


# 8) check_diags function
#checks diagonals for winState
#list->bool
def check_diags(board):
    winningLetter = " "
    if (" " != board[0] == board[4] == board[8]) or (" " != board[2] == board[4] == board[6]):
        winningLetter = board[4]
        return True, winningLetter
    else:
        return False, " "



# 10) board_full function
#checks if board is full of letters
#list->bool
def board_full(board):
    if " " not in board:
        return True
    else:
        return False


# 9) check_win function
#Checks who has won and if nobody does, draws the game
#list->bool
def check_win(board):
        winState = [check_cols(board), check_rows(board), check_diags(board)]
        winningLetter = " "
        for state in winState:
            #print(winState)
            if state[0]:
                winningLetter = state[1]
                return True, winningLetter
        if board_full(board):
            return True, "empty"
        else:
            return False, " "

#print(check_win([" "," "," "," "," "," "," "," "," "]))

#Randomly plays against the player
#list, str -> list
def ticTacToeAI(board, letter, playerLetter):
        randomSpot = 0
        while(board[randomSpot] != " " or board[randomSpot] == playerLetter):
            randomSpot = random.randrange(9)
        board[randomSpot] = letter
        return board
