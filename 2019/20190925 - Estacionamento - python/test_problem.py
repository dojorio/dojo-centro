#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def test_tamanho_1_eventos_1(self):
        tamanho = 1
        eventos = [('C', '1111', 1)]
        self.assertEqual(valor_total(tamanho, eventos), 10)

    def test_tamanho_2_eventos_1(self):
        tamanho = 1
        eventos = [('C', '1111', 2)]
        self.assertEqual(valor_total(tamanho, eventos), 0)

if __name__ == "__main__":
    unittest.main()
