# Project 3 - Tic-Tac-Toe Simulator
#
# Name: Raheel Rehmatullah
# Instructor: S. Einakian
# Section: 7

import unittest
from tictactoeFuncs import *

class TestCases(unittest.TestCase):
   def test_check_rows(self):
       self.assertEqual(check_rows(["x","x","x","o","o","x","x","o","o"]), (True, "x"))
       self.assertEqual(check_rows(["x","x","o","o","o","o","o","x","x"]), (True, "o"))
   def test_check_cols(self):
       self.assertEqual(check_cols(["x","x","x","o","o","x","x","o","o"]), (False, " "))
       self.assertEqual(check_cols(["o","x","x","o","o","x","o","o","o"]), (True, "o"))
   def test_check_diags(self):
       self.assertEqual(check_diags(["x","x","x","o","o","x","x","o","o"]), (False," "))
       self.assertEqual(check_diags(["o","x","x","o","o","x","o","o","o"]), (True, "o"))
   def test_board_full(self):
       self.assertEqual(board_full(["x","x","x","o","o","x","x","o","o"]), (True))
       self.assertEqual(board_full([" "," ","x","o","o","x","o","o","o"]), (False))
   def test_check_win(self):
       self.assertEqual(check_win(["x","x","x","o","o","x","x","o","o"]), (True, "x"))
       self.assertEqual(check_win(["o","x","x","o","o","x","o","o","o"]), (True,"o"))






# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
