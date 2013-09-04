# -*- coding: utf-8 -*-

class Guerra:
	def __init__(self):
		self.ladoA = set()
		self.ladoB = set()

	def sao_inimigos(self, pais1, pais2):
		self.ladoA.add(pais1)
		self.ladoB.add(pais2)

	def sao_amigos(self, pais1, pais2):
		self.ladoA.add(pais1)
		self.ladoA.add(pais2)

	def lados(self):
		return (self.ladoA, self.ladoB)
