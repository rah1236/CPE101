
# Name: Raheel Rehmatullah
# Section: 7

import unittest
import str_funcs


#You can dlete pass after wrinting your code
class TestCases(unittest.TestCase):
   def test_str_capitalize (self):
      self.assertEqual(str_funcs.str_capitalize("pee"), "Pee")
      self.assertEqual(str_funcs.str_capitalize("off the goop"), "Off The Goop")
      self.assertEqual(str_funcs.str_capitalize("snart"), "Snart")

   def test_vowel_extractor (self):
      self.assertEqual(str_funcs.vowel_extractor("pee"), "ee")
      self.assertEqual(str_funcs.vowel_extractor("off the goop"), "oeoo")
      self.assertEqual(str_funcs.vowel_extractor("snart"), "a")

   def test_str_rotate (self):
      self.assertEqual(str_funcs.str_rotate("pee"), "crr")
      self.assertEqual(str_funcs.str_rotate("off the goop"), "bss gur tbbc")
      self.assertEqual(str_funcs.str_rotate("snart"), "fnaeg")

   def test_make_substring (self):
      self.assertEqual(str_funcs.make_substring("pee", 1, 1, 1), "")
      self.assertEqual(str_funcs.make_substring("off the goop", 0, 1,1), "o")
      self.assertEqual(str_funcs.make_substring("snart", 0, 1, 2), "s")

   def test_is_palindrome (self):
      self.assertEqual(str_funcs.is_palindrome("pee"), False)
      self.assertEqual(str_funcs.is_palindrome("off the goop"), False)
      self.assertEqual(str_funcs.is_palindrome("poop"), True)

   def test_count_characters (self):
      self.assertEqual(str_funcs.count_characters("pee", "e"), 2)
      self.assertEqual(str_funcs.count_characters("off the goop", "o"), 3)
      self.assertEqual(str_funcs.count_characters("poop", "p"), 2)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
