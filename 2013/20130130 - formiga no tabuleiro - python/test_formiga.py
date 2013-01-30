#-*- coding: utf-8 -*-
import unittest
from formiga import formiga

class FormigaTestCase(unittest.TestCase):

	#linha, coluna = y, x
	
	def test_0_segundos(self):
		self.assertEqual((0, 0), formiga(0))

	def test_1_segundo(self):
		self.assertEqual((0, 1), formiga(1))

	def test_2_segundos(self):
		self.assertEqual((1, 1), formiga(2))

	def test_3_segundos(self):
		self.assertEqual((1, 0), formiga(3))

	def test_4_segundos(self):
		self.assertEqual((2, 0), formiga(4))

	def test_5_segundos(self):
		self.assertEqual((2, 1), formiga(5))

	def test_6_segundos(self):
		self.assertEqual((2, 2), formiga(6))

	def test_7_segundos(self):
		self.assertEqual((2, 1), formiga(6))

	def test_7_segundos(self):
		self.assertEqual((2, 1), formiga(6))


unittest.main()

