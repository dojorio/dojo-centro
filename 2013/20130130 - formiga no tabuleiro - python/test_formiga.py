#-*- coding: utf-8 -*-
import unittest
from formiga import formiga

class FormigaTestCase(unittest.TestCase):

	# coluna, linha = (x, y)

	def test_0_segundos(self):
		self.assertEqual((0, 0), formiga(0))

	def test_1_segundo(self):
		self.assertEqual((1, 0), formiga(1))

	def test_2_segundos(self):
		self.assertEqual((1, 1), formiga(2))

	def test_3_segundos(self):
		self.assertEqual((0, 1), formiga(3))

	def test_4_segundos(self):
		self.assertEqual((0, 2), formiga(4))

	def test_5_segundos(self):
		self.assertEqual((1, 2), formiga(5))

	def test_6_segundos(self):
		self.assertEqual((2, 2), formiga(6))

	def test_7_segundos(self):
		self.assertEqual((2, 1), formiga(7))

	def test_8_segundos(self):
		self.assertEqual((2, 0), formiga(8))

	def test_9_segundos(self):
		self.assertEqual((3, 0), formiga(9))

	def test_10_segundos(self):
		self.assertEqual((3, 1), formiga(10))

	def test_11_segundos(self):
		self.assertEqual((3, 2), formiga(11))

	def test_12_segundos(self):
		self.assertEqual((3, 3), formiga(12))

	def test_20_segundos(self):
		self.assertEqual((4, 4), formiga(20))

	def test_21_segundos(self):
		self.assertEqual((4, 3), formiga(21))

	def test_19_segundos(self):
		self.assertEqual((3, 4), formiga(19))

	def test_1_bilhao_de_segundos(self):
		self.assertEqual((31622, 14128), formiga(10**9))


unittest.main()

