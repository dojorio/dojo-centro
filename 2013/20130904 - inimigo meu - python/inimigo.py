# -*- coding: utf-8 -*-

class Guerra:
	def __init__(self):
		self.lados = []

	def sao_inimigos(self, pais1, pais2):
		self.lados.append({pais1})
		self.lados.append({pais2})

		if pais1 in self.ladoA or pais2 in self.ladoB:
			self.ladoA.add(pais1)
			self.ladoB.add(pais2)
		else:
			self.ladoB.add(pais1)
			self.ladoA.add(pais2)

	def sao_amigos(self, pais1, pais2):
		self.lados.append({pais1, pais2})

		if pais1 in self.ladoA or pais2 in self.ladoA:
			self.ladoA.add(pais1)
			self.ladoA.add(pais2)
		else:
			self.ladoB.add(pais1)
			self.ladoB.add(pais2)

	def lados(self):
		return (self.ladoA, self.ladoB)
