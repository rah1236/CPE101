# Project 3 - Tic-Tac-Toe Simulator
#
# Name: Raheel Rehmatullah
# Instructor: S. Einakian
# Section: 7
import time
import unittest
from tictactoeFuncs import *

def main():

    board = create_board()
    if welcome() == "2":

        playerLetter = pick_letter()
        if playerLetter == "x":
            opLetter = "o"
        else:
            opLetter = "x"
            print_board(board)
        while(check_win(board)):
            print("Your turn.")
            get_input(board, playerLetter, opLetter)
            print_board(board)
            if check_win(board)[0] and check_win(board)[1] == " ":
                print("Draw!, Thanks for playing.")
                break
            elif check_win(board)[0] and check_win(board)[1] == opLetter:
                print("You lose! Sorry!")
                break
            elif check_win(board)[0] and check_win(board)[1] == playerLetter:
                print("You win! Thanks for playing!")
                break


            print("Next Player's Turn")
            time.sleep(2)
            get_input(board, opLetter, playerLetter)
            print_board(board)
            if check_win(board)[0] and check_win(board)[1] == " ":
                print("Draw!, Thanks for playing.")
                break
            elif check_win(board)[0] and check_win(board)[1] == opLetter:
                print("You lose! Sorry!")
                break
            elif check_win(board)[0] and check_win(board)[1] == playerLetter:
                print("You win! Thanks for playing!")
                break
    else:
        playerLetter = pick_letter()
        if playerLetter == "x":
            opLetter = "o"
        else:
            opLetter = "x"
            print_board(board)
        while(check_win(board)):
            print("Your turn.")
            get_input(board, playerLetter, opLetter)
            print_board(board)
            if check_win(board)[0] and check_win(board)[1] == " ":
                print("Draw!, Thanks for playing.")
                break
            elif check_win(board)[0] and check_win(board)[1] == opLetter:
                print("You lose! Sorry!")
                break
            elif check_win(board)[0] and check_win(board)[1] == playerLetter:
                print("You win! Thanks for playing!")
                break


            print("CPU Turn")
            time.sleep(2)
            ticTacToeAI(board, opLetter, playerLetter)
            print_board(board)
            if check_win(board)[0] and check_win(board)[1] == " ":
                print("Draw!, Thanks for playing.")
                break
            elif check_win(board)[0] and check_win(board)[1] == opLetter:
                print("You lose! Sorry!")
                break
            elif check_win(board)[0] and check_win(board)[1] == playerLetter:
                print("You win! Thanks for playing!")
                break






if __name__ == '__main__':
    main()
