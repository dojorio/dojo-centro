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

