#-*- coding: utf-8 -*-
import unittest
from esquibunda import esquibunda

class EsquibundaTestCase(unittest.TestCase):
	def test_planicie(self):
		montanha = []
		self.assertEquals(0, esquibunda(montanha))

	def test_lombada(self):
		montanha = [
			[1]
		]
		self.assertEquals(1, esquibunda(montanha))


unittest.main()
