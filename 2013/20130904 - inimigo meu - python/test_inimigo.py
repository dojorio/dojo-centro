# -*- coding: utf-8 -*-
import unittest
from inimigo import Guerra

class TestInimigo(unittest.TestCase):
	def test_dois_paises(self):
		guerra = Guerra('A', 'B')
		guerra.sao_inimigos('A', 'B')
		self.assertEqual({{'A'},{'B'}}, guerra.lados())

unittest.main()
