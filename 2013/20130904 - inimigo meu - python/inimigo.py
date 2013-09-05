# -*- coding: utf-8 -*-

class Guerra:
	def __init__(self):
		self.ladoA = set()
		self.ladoB = set()
		self.relacoes = []
		self.panelinhas = {}


	def sao_inimigos(self, pais1, pais2):
		self.unir(('inimigos', pais1), pais2)
		self.unir(pais1, ('inimigos', pais2))

	def sao_amigos(self, pais1, pais2):
		self.unir(pais1, pais2)
		self.unir(('inimigos', pais1), ('inimigos', pais2))

	def unir(self, pais1, pais2):
		if pais1 not in self.panelinhas:
			self.panelinhas[pais1] = {pais1}
		if pais2 not in self.panelinhas:
			self.panelinhas[pais2] = {pais2}

		unidos = self.panelinhas[pais1].union(self.panelinhas[pais2])
		for pais in unidos:
			self.panelinhas[pais] = unidos

	def lados(self):
		print self.panelinhas
		ladoA = set()
		ladoB = set()

		for relacao, pais1, pais2 in self.relacoes:
			if relacao == 'amigo':
				ladoA.add(pais1)
				ladoA.add(pais2)
			else:
				ladoA.add(pais1)
				ladoB.add(pais2)

		return ladoA, ladoB
