#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

if __name__ == "__main__":
    unittest.main()
