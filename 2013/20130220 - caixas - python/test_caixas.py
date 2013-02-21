#-*- coding: utf-8 -*-
import unittest
from caixas import empilhar, Caixa

class CaixasTestCase(unittest.TestCase):

	def test_nenhuma_caixa(self):
		caixas = []
		resultado = empilhar(caixas)
		self.assertEquals(0, resultado)

	def test_uma_caixa(self):
		caixas = [Caixa(1, 1)]
		resultado = empilhar(caixas)
		self.assertEquals(1, resultado)

	def test_duas_caixas(self):
		caixas = [Caixa(2, 1), Caixa(2, 1)]
		self.assertEquals(1, empilhar(caixas))

	def test_duas_caixas_que_empilham(self):
		caixas = [Caixa(2, 1), Caixa(1, 1)]
		self.assertEquals(2, empilhar(caixas))

	def test_duas_caixas_que_empilham_invertido(self):
		caixas = [Caixa(1, 1), Caixa(2, 1)]
		self.assertEquals(2, empilhar(caixas))

	def test_tres_caixas_que_nao_empilham(self):
		caixas = [Caixa(2, 1), Caixa(2, 1), Caixa(2, 1)]
		self.assertEquals(1, empilhar(caixas))

	def test_tres_caixas_que_empilham_duas(self):
		caixas = [Caixa(2, 1), Caixa(2, 1), Caixa(1, 1)]
		self.assertEquals(2, empilhar(caixas))

	def test_tres_caixas_que_empilham_duas_2(self):
		caixas = [Caixa(10, 5), Caixa(3, 4), Caixa(3, 3)]
		self.assertEquals(2, empilhar(caixas))

	def test_tres_caixas_que_empilham_duas_3(self):
		caixas = [Caixa(10, 5), Caixa(6, 4), Caixa(6, 6)]
		self.assertEquals(2, empilhar(caixas))

unittest.main()