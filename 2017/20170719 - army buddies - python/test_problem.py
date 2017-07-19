#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://www.urionlinejudge.com.br/judge/en/problems/view/1311

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_1_soldado_1_baixa(self):
        baixas = [(1, 1)]
        self.assertEqual(army_buddies(1, baixas), ['* *'])

    def test_2_soldados_1_baixa(self):
        baixas = [(1, 1)]
        self.assertEqual(army_buddies(2, baixas), ['* 2'])


if __name__ == "__main__":
    unittest.main()

