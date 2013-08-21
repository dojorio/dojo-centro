# -*- coding: utf-8 -*-
import unittest
from catdog import votacao

class TestCatDog(unittest.TestCase):
	def test_0_voto(self):
		votos = []
		self.assertEqual(0, votacao(0, 0, votos))

	def test_1_voto(self):
		votos = [('G1', 'C1')]
		self.assertEqual(1, votacao(1, 1, votos))


unittest.main()
