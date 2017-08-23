#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_1_minuto(self):
        value = '1 1 1 2'
        expected = 'O JOGO DUROU 0 HORA(S) E 1 MINUTO(S)'
        self.assertEqual(expected, time(value))

    def test_2_minuto(self):
        value = '1 1 1 3'
        expected = 'O JOGO DUROU 0 HORA(S) E 2 MINUTO(S)'
        self.assertEqual(expected, time(value))

    def test_3_minuto(self):
        value = '1 1 1 4'
        expected = 'O JOGO DUROU 0 HORA(S) E 3 MINUTO(S)'
        self.assertEqual(expected, time(value))

    def test_4_minuto(self):
        value = '1 1 1 5'
        expected = 'O JOGO DUROU 0 HORA(S) E 4 MINUTO(S)'
        self.assertEqual(expected, time(value))

if __name__ == "__main__":
    unittest.main()

