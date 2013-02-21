#-*- coding: utf-8 -*-

class Caixa(object):
	def __init__(self, peso, capacidade):
		self.peso = peso
		self.capacidade = capacidade

INFINITO = 1e300

def empilhar(caixas):
	caixas.sort(key=lambda caixa: (-caixa.capacidade, -caixa.peso))

	pilha = INF
	tamanho = 0

	for caixa in caixas:
		if caixa.peso <= pilha:
			pilha = min(pilha - caixa.peso, caixa.capacidade)
			tamanho += 1

	return tamanho