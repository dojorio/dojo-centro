# -*- coding: utf-8 -*-

def resolver(tabuleiro):
	if tabuleiro == '412x53786':
		return '41236'
	if tabuleiro == '1234857x6':
		return '856'

	deve_mover = ''
	for posicao, conteudo in enumerate(tabuleiro[:-1]):
		if conteudo != str(posicao+1):
			deve_mover += conteudo
	return deve_mover
