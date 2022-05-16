# Project 3 - Tic-Tac-Toe Simulator
#
# Name: Raheel Rehmatullah
# Instructor: S. Einakian
# Section: 7
# Functions definitions comes here

# 1) welcome function
#Welcomes user into program
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
def create_board():
    return [" "," "," "," "," "," "," "," "," "]


# 3) print_board function
def print_board(board):

        print("""
       {0} |  {1}  | {2}
    -----------------
       {3} |  {4}  | {5}
    -----------------
       {6} |  {7}  | {8}""".format(*board))


print_board(create_board())

# 4) pick_etter function
#your codes goes here


# 5) get_input function
#your codes goes here


# 6) check_rows function
#your codes goes here


# 7) check_cols function
#your codes goes here


# 8) check_diags function
#your codes goes here


# 9) check_win function
#your codes goes here


# 10) board_full function
#your codes goes here
