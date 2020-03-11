#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.dojopuzzles.com/problemas/exibe/poker/

import unittest
from problem import *

# D = Diamonds = ouros
# H = Hearts = copas
# S = Spades = espadas
# C = ? = paus

class TestProblem(unittest.TestCase):
    def test_hand_value_1(self):
        hand = ['2D','3C', '4H', '5S', '6D']
        self.assertEqual(hand_value(hand), 'carta-alta')

    def test_hand_value_2(self):
        hand = ['2D','3C', '4H', '5S', '6D']
        self.assertEqual(hand_value(hand), 'carta-alta')

if __name__ == "__main__":
    unittest.main()

