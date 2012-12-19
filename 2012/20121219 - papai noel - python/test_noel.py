#coding: utf-8
import unittest
from noel import noel
from math import sqrt

class NoelTestCase(unittest.TestCase):

    def test_uma_crianca(self):
        criancas = [(1, 0)]
        self.assertEqual(1, noel(criancas))

    def test_uma_crianca_longe(self):
        criancas = [(2, 0)]
        self.assertEqual(2, noel(criancas))

    def test_uma_crianca_pra_cima(self):
        criancas = [(0, 1)]
        self.assertEqual(1, noel(criancas))

    def test_uma_crianca_pra_cima(self):
        criancas = [(1, 1)]
        self.assertEqual(sqrt(2), noel(criancas))

unittest.main()