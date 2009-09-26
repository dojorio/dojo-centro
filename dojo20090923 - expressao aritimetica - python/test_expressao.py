# -*- coding: utf-8 -*-
import unittest

from expressao import *

class TesteExpressao(unittest.TestCase):
	def teste_2_mais_2_igual_a_4(self):
		self.assertEqual(4, avaliador("2+2"))
		
	def teste_2_mais_5_igual_a_7(self):
		self.assertEqual(7, avaliador("2+5"))
		
	def teste_2_igual_a_2(self):
		self.assertEqual(2, avaliador("2"))
		
	def teste_4_igual_a_4(self):
		self.assertEqual(4, avaliador("4"))
		
	def teste_42_igual_a_42(self):
		self.assertEqual(42, avaliador("42"))
		
	def teste_42_igual_a_42(self):
		self.assertEqual(-42, avaliador("-42"))
		
	def teste_1_menos_0_igual_a_1(self):
		self.assertEqual(1, avaliador("1-0"))
		
	def teste_22_igual_a_22(self):
		self.assertEqual(22, avaliador("22"))

	def teste_15_menos_5_igual_a_10(self):
		self.assertEqual(10, avaliador("15-5"))
		
	def teste_15_menos_5_menos_5_igual_a_5(self):
		self.assertEqual(5, avaliador("15-5-5"))
	def teste_15_menos_5_mais_5_igual_a_15(self):
		self.assertEqual(15, avaliador("15-5+5"))
	def teste_menos15_menos_5_mais_5_igual_a_menos15(self):
		self.assertEqual(-15, avaliador("-15-5+5"))	
unittest.main()