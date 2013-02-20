#-*- coding: utf-8 -*-

class Caixa(object):
	def __init__(self, peso, capacidade):
		self.peso = peso
		self.capacidade = capacidade

def empilhar(caixas):
	empilhavel = caixas[1].peso <= caixas[0].capacidade
	if len(caixas) > 1 and not empilhavel:
		return 1

	return len(caixas)