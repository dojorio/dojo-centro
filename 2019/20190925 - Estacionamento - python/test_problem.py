#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1246

import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def test_tamanho_1_eventos_1(self):
        tamanho = 1
        eventos = [('C', '1111', 1)]
        self.assertEqual(valor_total(tamanho, eventos), 10)

    def test_tamanho_1_eventos_2(self):
        tamanho = 1
        eventos = [('C', '1111', 2)]
        self.assertEqual(valor_total(tamanho, eventos), 0)

    def test_tamanho_2_eventos_1(self):
        tamanho = 2
        eventos = [('C', '1111', 1)]
        self.assertEqual(valor_total(tamanho, eventos), 10)

    def test_tamanho_2_eventos_1_1(self):
        tamanho = 2
        eventos = [('C', '1111', 1), ('C', '1112', 1)]
        self.assertEqual(valor_total(tamanho, eventos), 20)

    def test_tamanho_2_eventos_1_2(self):
        tamanho = 2
        eventos = [('C', '1111', 1), ('C', '1112', 2)]
        self.assertEqual(valor_total(tamanho, eventos), 10)

    def test_tamanho_2_eventos_1_S(self):
        tamanho = 2
        eventos = [('C', '1111', 1), ('S', '1111')]
        self.assertEqual(valor_total(tamanho, eventos), 10)

    def test_tamanho_2_eventos_3_1S(self):
        tamanho = 2
        eventos = [('C', '1111', 1), ('S', '1111'), ('C', '1112', 2)]
        self.assertEqual(valor_total(tamanho, eventos), 20)

    def test_tamanho_3_eventos_4_1S(self):
        tamanho = 3
        eventos = [('C', '1111', 1), ('C', '1112', 2), ('S', '1111'), ('C', '1113', 2)]
        self.assertEqual(valor_total(tamanho, eventos), 20)

    def test_tamanho_3_eventos_3_1S(self):
        tamanho = 3
        eventos = [('C', '1111', 1), ('C', '1112', 1), ('S', '1111'), ('C', '1113', 2)]
        self.assertEqual(valor_total(tamanho, eventos), 20)

    def test_tamanho_10_eventos_7(self):
        tamanho = 10
        eventos = [
            ('C', '1234', 5),
            ('C', '1111', 4),
            ('C', '2222', 4),
            ('C', '4321', 3),
            ('S', '1111'),
            ('C', '2002', 6),
            ('C', '4321', 3)
        ]
        self.assertEqual(valor_total(tamanho, eventos), 30)        

    def test_tamanho_20_eventos_10(self):
        tamanho = 20
        eventos = [
            ('C', '1234', 20),
            ('C', '5678', 1),
            ('S', '1234'),
            ('C', '1234', 20),
            ('C', '5678', 1),
            ('S', '1234'),
            ('C', '5678', 1),
            ('C', '1234', 20),
            ('C', '5555', 1),
            ('S', '5678')
        ]
        self.assertEqual(valor_total(tamanho, eventos), 40)   

if __name__ == "__main__":
    unittest.main()
