# -*- coding: utf-8 -*-

import unittest
from skyline import skyline

class TestSkyline(unittest.TestCase):
	def test_no_buildings(self):
		saida = skyline([])
		esperado = []
		self.assertEqual(esperado, saida)

	def test_one_building(self):
		saida = skyline([(0, 1, 1)])
		esperado = [(0,1), (1, 0)]
		self.assertEqual(esperado, saida)

unittest.main()


