# -*- coding: utf-8 -*-

class Guerra:
	def __init__(self, *paises):
		pass

	def sao_inimigos(self, pais1, pais2):
		self.pais1 = [pais1]
		self.pais2 = [pais2]

	def sao_amigos(self, pais1, pais2):
		self.pais1 = [pais1, pais2]
		self.pais2 = []

	def lados(self):
		return (self.pais1, self.pais2)
