# -*- coding: utf-8 -*-

class Guerra:
	def __init__(self):
		self.ladoA = set()
		self.ladoB = set()
		self.relacoes = []


	def sao_inimigos(self, pais1, pais2):
		self.relacoes.append(('inimigo', pais1, pais2))


	def sao_amigos(self, pais1, pais2):
		self.relacoes.append(('amigo', pais1, pais2))

	def lados(self):
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
