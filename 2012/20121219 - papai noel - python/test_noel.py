#coding: utf-8
import unittest
from noel import noel

class NoelTestCase(unittest.TestCase):
    def test_uma_crianca(self):
        criancas = {'joao': (1, 0)}
        esperado = [('noel', 'joao')]
        self.assertEqual(set(esperado), noel(criancas))

unittest.main()