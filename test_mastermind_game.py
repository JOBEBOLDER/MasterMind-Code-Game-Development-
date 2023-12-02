"""
CS5001
   Fall 2023
   Jieyao chen
   final project: test MasterMind Code Game
   will create functions that use lists to create, shuffle,
   and deal cards to a number up to 4 “hands”.
"""

import unittest
from mastermind_game import confirm_answer

class Testmastermind(unittest.TestCase):
    def test_correct_guess(self):
        secret_code = ['red' , ]
