#-*- coding: utf-8 -*-

class Caixa(object):
	def __init__(self, peso, capacidade):
		self.peso = peso
		self.capacidade = capacidade

INFINITO = 1e300

def empilhar(caixas):
	caixas_sort_capacidade = caixas.sort(key=lambda caixa: (-caixa.capacidade, -caixa.peso))

	capacidade_da_pilha = INFINITO
	tamanho_da_pilha = 0

	for caixa in caixas_sort_capacidade:
		if caixa.peso <= capacidade_da_pilha:
			capacidade_da_pilha = min(
				capacidade_da_pilha - caixa.peso, caixa.capacidade)
			tamanho_da_pilha += 1

	return tamanho_da_pilha