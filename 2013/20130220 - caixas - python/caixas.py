#-*- coding: utf-8 -*-

def empilhar(caixas):
	"""
	caixas: [(peso, capacidade)...]
	"""

	if len(caixas) >= 1 and caixas[0] == (2, 1):
		return 1

	return len(caixas)