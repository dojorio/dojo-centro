#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from problem import *

# https://github.com/jonatasemidio/dojo_problems/blob/master/escudo-anti-bruxas.md
class TestProblem(unittest.TestCase):
    def test_bruxa_wins_0_0(self):
        criancas = [(0, 0)]
        sal = 0
        self.assertEqual(
            escudo_antibruxa(criancas, sal),
            BRUXA_WINS
        )

    def test_kids_win_0_0(self):
        criancas = [(0, 0)]
        sal = 8
        self.assertEqual(
            escudo_antibruxa(criancas, sal),
            KIDS_WIN
        )

    def test_kids_win_0_0_again(self):
        criancas = [(0, 0)]
        sal = 9
        self.assertEqual(
            escudo_antibruxa(criancas, sal),
            KIDS_WIN
        )

    def test_kids_win_0_0_again_again(self):
        criancas = [(0, 0)]
        sal = 10
        self.assertEqual(
            escudo_antibruxa(criancas, sal),
            KIDS_WIN
        )

    def test_kids_win_0_0_again_11(self):
        criancas = [(0, 0)]
        sal = 11
        self.assertEqual(
            escudo_antibruxa(criancas, sal),
            KIDS_WIN
        )

    def test_bruxa_wins_two_kids(self):
        criancas = [(0, 0), (1, 0)]
        sal = 8
        self.assertEqual(
            escudo_antibruxa(criancas, sal),
            BRUXA_WINS
        )

    def test_kids_win(self):
        criancas = [(0, 0), (1, 0)]
        sal = 10
        self.assertEqual(
            escudo_antibruxa(criancas, sal),
            KIDS_WIN
        )

    def test_kids_wins_diff_order(self):
        criancas = [(1, 0), (0, 0)]
        sal = 10
        self.assertEqual(
            escudo_antibruxa(criancas, sal),
            KIDS_WIN
        )

    def test_bruxa_wins_x(self):
        criancas = [(0, 0), (2, 0)]
        sal = 10
        self.assertEqual(
            escudo_antibruxa(criancas, sal),
            BRUXA_WINS
        )

    def test_bruxa_wins_x_criancas_escape(self):
        criancas = [(0, 0), (2, 0)]
        sal = 12
        self.assertEqual(
            escudo_antibruxa(criancas, sal),
            KIDS_WIN
        )


if __name__ == "__main__":
    unittest.main()