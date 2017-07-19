#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://www.urionlinejudge.com.br/judge/en/problems/view/1311

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_1_soldado_1_baixa(self):
        baixas = [(1, 1)]
        self.assertEqual(['* *'], army_buddies(1, baixas))

    def test_2_soldados_1_baixa(self):
        baixas = [(1, 1)]
        self.assertEqual(['* 2'], army_buddies(2, baixas))

    def test_2_soldados_a_outra_1_baixa(self):
        baixas = [(2, 2)]
        self.assertEqual(['1 *'], army_buddies(2, baixas))

    def test_3_soldados_1_baixa(self):
        baixas = [(1, 1)]
        self.assertEqual(['* 2'], army_buddies(3, baixas))

    def test_4_soldados_1_baixa(self):
        baixas = [(1, 1)]
        self.assertEqual(['* 2'], army_buddies(4, baixas))
    
    def test_5_soldados_1_baixa(self):
        baixas = [(1, 1)]
        self.assertEqual(['* 2'], army_buddies(5, baixas))
    
    def test_3_soldados_ultimo_morre(self):
        soldados = 3
        baixas = [(3, 3)]
        self.assertEqual(['2 *'], army_buddies(soldados, baixas)) 
    
    def test_4_soldados_ultimo_morre(self):
        soldados = 4
        baixas = [(4, 4)]
        self.assertEqual(['3 *'], army_buddies(soldados, baixas))

    def test_3_soldados_meio_morre(self):
        soldados = 3
        baixas = [(2, 2)]
        self.assertEqual(['1 3'], army_buddies(soldados, baixas)) 

if __name__ == "__main__":
    unittest.main()

