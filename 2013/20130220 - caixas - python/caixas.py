#-*- coding: utf-8 -*-

class Caixa(object):
	def __init__(self, peso, capacidade):
		self.peso = peso
		self.capacidade = capacidade

	def suporta(self, caixa):
		return self.capacidade >= caixa.peso

def empilhar(caixas):
	pilha = 0
	sort(caixas, key=lambda caixa: -caixa.capacidade)
	if len(caixas) > 1:
		empilhavel = caixas[0].suporta(caixas[1])
		
		if not empilhavel:
			return 1

	return len(caixas)