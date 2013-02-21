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

	capacidade_pilha = caixas[0].capacidade if caixas else 0

	for caixa in caixas:
		pilha_vazia = not pilha
		cabe_na_pilha = caixa.peso <= capacidade_pilha
		suporta_caixa = pilha[-1].suporta(caixa)


		if pilha_vazia or (cabe_na_pilha and suporta_caixa):
			pilha.append(caixa)

			if len(pilha) > 1:
				capacidade_pilha -= caixa.peso

	return len(pilha)