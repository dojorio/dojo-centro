from unittest import TestCase
import unittest
from vaium import *

class TesteVaium(TestCase):
	def testeSoma(self):
		self.assertEqual(soma(5,7),12)
	
	def testeVerificaSoma(self):
		self.assertEqual(verificaSoma(4,8),True)
		self.assertEqual(verificaSoma(2,2),False)
	def testeContaDigito(self):
		self.assertEqual(contaDigito(11),2)
		self.assertEqual(contaDigito(111),3)
		self.assertEqual(contaDigito(-111),3) 
	def testeNumeroParaArray(self):
		self.assertEqual(NumeroParaArray(302),[3,0,2])
		self.assertEqual(NumeroParaArray(-302),[3,0,2])
		
	def testeSomaArray(self):
		a = 5
		b = 8
		self.assertEqual(SomaArray(a,b),(a+b))
		a=20
		b=40
		self.assertEqual(SomaArray(a,b),(a+b))
unittest.main()