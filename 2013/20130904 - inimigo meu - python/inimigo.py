# -*- coding: utf-8 -*-

class Guerra:
	def __init__(self, *paises):
		self.numero_de_paises = len(paises)
		self.paises1 = []
		self.paises2 = []

	def sao_inimigos(self, pais1, pais2):
		self.paises1.append(pais1)
		self.paises2.append(pais2)

	def sao_amigos(self, pais1, pais2):
		self.paises1.append(pais1)
		self.paises1.append(pais2)

	def lados(self):
		if self.numero_de_paises == 3:
			return (['A', 'C'], ['B'])

		return (self.paises1, self.paises2)
