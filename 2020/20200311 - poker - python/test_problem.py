#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.dojopuzzles.com/problemas/exibe/poker/

import unittest
from problem import *

# D = Diamonds = ouros
# H = Hearts = copas
# S = Spades = espadas
# C = ? = paus

class TestHandValue(unittest.TestCase):
    def test_hand_value_1(self):
        hand = ['2D','3C', '4H', '5S', '6D']
        self.assertEqual(hand_value(hand), 'carta-alta')

    def test_hand_value_2(self):
        hand = ['2D','2C', '4H', '5S', '6D']
        self.assertEqual(hand_value(hand), 'par')

    def test_hand_value_3(self):
        hand = ['2D','3C', '4H', '5S', '2D']
        self.assertEqual(hand_value(hand), 'par')

    def test_hand_value_4(self):
        hand = ['2D','3C', '4H', '5S', '3D']
        self.assertEqual(hand_value(hand), 'par')

    def test_hand_value_5(self):
        hand = ['2D','4C', '4H', '5S', '3D']
        self.assertEqual(hand_value(hand), 'par')

    def test_hand_value_6(self):
        hand = ['2D','4C', '5H', '5S', '3D']
        self.assertEqual(hand_value(hand), 'par')

    def test_hand_value_7(self):
        hand = ['2D','3C', '5H', '5S', '3D']
        self.assertEqual(hand_value(hand), 'dois-pares')

    def test_hand_value_8(self):
        hand = ['2D','5C', '5H', '5S', '3D']
        self.assertEqual(hand_value(hand), 'trinca')
            

class TestSortHand(unittest.TestCase):
    def test_sort_hand_1(self):
        hand = ['2D','3C', '4H', '5S', '6D']
        self.assertEqual(sort_hand(hand), ['6D', '5S', '4H', '3C', '2D'])

    def test_sort_hand_2(self):
        hand = ['2D','3C', 'TH', '5S', '6D']
        self.assertEqual(sort_hand(hand), ['TH', '6D', '5S', '3C', '2D'])

    def test_sort_hand_3(self):
        hand = ['2D','3C', 'TH', 'JS', '6D']
        self.assertEqual(sort_hand(hand), [ 'JS', 'TH', '6D', '3C', '2D'])

    def test_sort_hand_4(self):
        hand = ['QD','3C', 'TH', 'JS', '6D']
        self.assertEqual(sort_hand(hand), ['QD', 'JS', 'TH', '6D', '3C'])        

    def test_sort_hand_5(self):
        hand = ['QD','3C', 'TH', 'JS', 'KD']
        self.assertEqual(sort_hand(hand), ['KD', 'QD', 'JS', 'TH', '3C'])

    def test_sort_hand_6(self):
        hand = ['QD','AC', 'TH', 'JS', 'KD']
        self.assertEqual(sort_hand(hand), ['AC', 'KD', 'QD', 'JS', 'TH'])

if __name__ == "__main__":
    unittest.main()

