#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1167

import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def test_criancas_1_2(self):
        criancas = {
            'Jose': 1,
            'Joao': 2
        }
        self.assertEqual('Jose', gira(criancas))

    def test_criancas_1_2_trocado(self):
        criancas = {
            'Joao': 1,
            'Jose': 2
        }
        self.assertEqual('Joao', gira(criancas))

    def test_criancas_2_2(self):
        criancas = {
            'Joao': 2,
            'Jose': 2
        }
        self.assertEqual('Jose', gira(criancas))

    def test_criancas_4_2(self):
        criancas = {
            'Joao': 4,
            'Jose': 2
        }
        self.assertEqual('Jose', gira(criancas))

    def test_criancas_1_1_1(self):
        criancas = {
            'Joao': 1,
            'Jose': 1,
            'Maria': 1,
        }
        self.assertEqual('Joao', gira(criancas))

    def test_criancas_2_1_1(self):
        criancas = {
            'Joao': 2,
            'Jose': 1,
            'Maria': 1,
        }
        self.assertEqual('Joao', gira(criancas))



if __name__ == "__main__":
    unittest.main()
