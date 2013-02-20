#-*- coding: utf-8 -*-

class Caixa(object):
	def __init__(self, peso, capacidade):
		self.peso = peso
		self.capacidade = capacidade

	def suporta(self, caixa):
		return self.capacidade >= caixa.peso

def empilhar(caixas):
	caixas.sort(key=lambda caixa: (-caixa.capacidade, -caixa.peso))

	pilha = []
	for caixa in caixas:
		if not pilha or pilha[-1].suporta(caixa):
			pilha.append(caixa)

	return len(pilha)