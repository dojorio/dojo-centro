#-*- coding: utf-8 -*-

class Caixa(object):
	def __init__(self, peso, capacidade):
		self.peso = peso
		self.capacidade = capacidade

	def suporta(self, caixa):
		return self.capacidade >= caixa.peso

def empilhar(caixas):
	if len(caixas) > 1 and not (caixas[0].suporta(caixas[1]) or
							    caixas[1].suporta(caixas[0])):
		return 1

	return len(caixas)