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

	def test_1_voto_2_gatos(self):
		votos = [('G1', 'C1')]
		self.assertEqual(1, votacao(2, 1, votos))

	def test_1_voto_2_caes_2_gatos(self):
		votos = [('G1','C1')]
		self.assertEqual(1, votacao(2, 2, votos))

	def test_2_votos_2_caes_2_gatos(self):
		votos = [('G1', 'C1'), ('C1', 'G1')]
		self.assertEqual(1, votacao(2, 2, votos))

	def test_2_votos_diferentes_2_caes_2_gatos(self):
		votos = [('G1', 'C2'), ('C1', 'G1')]
		self.assertEqual(1, votacao(2, 2, votos))

	def test_3_votos_2_atendidos_2_caes_2_gatos(self):
		votos = [('G1', 'C1'), ('C1', 'G2'), ('G2', 'C2')]
		self.assertEqual(2, votacao(2, 2, votos))

	def test_3_votos_iguais(self):
		votos = [('G1', 'C1'), ('G1', 'C1'), ('G1', 'C1')]
		self.assertEqual(3, votacao(1, 1, votos))

	def test_3_votos_2_atendidos_2_caes_2_gatos(self):
		votos = [('G1', 'C1'), ('G2', 'C2'), ('C1', 'G2')]
		self.assertEqual(2, votacao(2, 2, votos))


unittest.main()
