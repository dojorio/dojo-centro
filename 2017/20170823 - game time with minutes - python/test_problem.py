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

    def test_10_minuto(self):
        value = '1 1 1 11'
        expected = 'O JOGO DUROU 0 HORA(S) E 10 MINUTO(S)'
        self.assertEqual(expected, time(value))

    def test_1_hora(self):
        value = '1 1 2 1'
        expected = 'O JOGO DUROU 1 HORA(S) E 0 MINUTO(S)'
        self.assertEqual(expected, time(value))

    def test_2_hora(self):
        value = '1 1 3 1'
        expected = 'O JOGO DUROU 2 HORA(S) E 0 MINUTO(S)'
        self.assertEqual(expected, time(value))

    def test_50_minutos(self):
        value = '1 50 2 40'
        expected = 'O JOGO DUROU 0 HORA(S) E 50 MINUTO(S)'
        self.assertEqual(expected, time(value))

if __name__ == "__main__":
    unittest.main()

