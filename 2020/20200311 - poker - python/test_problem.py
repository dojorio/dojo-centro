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

    def test_higher_card_1(self):
        hand = ['2D','3C', '4H', '5S', '6D']
        self.assertEqual(sort_hand(hand), ['6D', '5S', '4H', '3C', '2D'])

    def test_higher_card_2(self):
        hand = ['2D','3C', 'TH', '5S', '6D']
        self.assertEqual(sort_hand(hand), ['TH', '6D', '5S', '3C', '2D'])

    def test_higher_card_3(self):
        hand = ['2D','3C', 'TH', 'JS', '6D']
        self.assertEqual(sort_hand(hand), [ 'JS', 'TH', '6D', '3C', '2D'])

    def test_higher_card_4(self):
        hand = ['QD','3C', 'TH', 'JS', '6D']
        self.assertEqual(sort_hand(hand), ['QD', 'JS', 'TH', '6D', '3C'])        

    def test_higher_card_5(self):
        hand = ['QD','3C', 'TH', 'JS', 'KD']
        self.assertEqual(sort_hand(hand), ['KD', 'QD', 'JS', 'TH', '3C'])

    def test_higher_card_6(self):
        hand = ['QD','AC', 'TH', 'JS', 'KD']
        self.assertEqual(sort_hand(hand), ['AC', 'KD', 'QD', 'JS', 'TH'])

    def test_hand_value_2(self):
        hand = ['2D','2C', '4H', '5S', '6D']
        self.assertEqual(hand_value(hand), 'par')    

if __name__ == "__main__":
    unittest.main()

