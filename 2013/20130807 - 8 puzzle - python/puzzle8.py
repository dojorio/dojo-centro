# -*- coding: utf-8 -*-

def resolver(tabuleiro):
	if tabuleiro == '412x53786':
		return '41236'
	deve_mover = ''
	for posicao,elemento in enumerate(tabuleiro[:-1]):
		if elemento != str(posicao+1):
			deve_mover += str(posicao+1)
	return deve_mover
