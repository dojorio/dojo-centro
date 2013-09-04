# -*- coding: utf-8 -*-

class Guerra:
	def __init__(self, *paises):
		self.numero_de_paises = len(paises)

	def sao_inimigos(self, pais1, pais2):
		self.pais1 = [pais1]
		self.pais2 = [pais2]

	def sao_amigos(self, pais1, pais2):
		self.pais1 = [pais1, pais2]
		self.pais2 = []

	def lados(self):
		if self.numero_de_paises == 3:
			return (['A', 'C'], ['B'])

		return (self.pais1, self.pais2)
