# -*- coding: utf-8 -*-
import unittest
from inimigo import Guerra

class TestInimigo(unittest.TestCase):
	def test_dois_paises(self):
		guerra = Guerra('A', 'B')
		guerra.sao_inimigos('A', 'B')
		self.assertEqual((['A'],['B']), guerra.lados())

	def test_dois_paises2(self):
		guerra = Guerra('A', 'C')
		guerra.sao_inimigos('A', 'C')
		self.assertEqual((['A'],['C']), guerra.lados())

unittest.main()
