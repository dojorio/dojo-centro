#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_permutacoes_de_um_numero(self):
        self.assertEqual(['1'], permutacoes('1'))

    def test_permutacoes_de_dois_digitos(self):
        self.assertEqual(['12', '21'], permutacoes('12'))

    def test_permutacoes_de_outros_dois_digitos(self):
        self.assertEqual(['24', '42'], permutacoes('24'))

    def test_permutacoes_de_mais_outros_dois_digitos(self):
        self.assertEqual(['24', '42'], permutacoes('42'))

    def test_permutacoes_de_tres_digitos(self):
        self.assertEqual(['259', '295', '529', '592', '925', '952'],
                         permutacoes('529'))




if __name__ == "__main__":
    unittest.main()

