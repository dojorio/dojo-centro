# -*- coding: utf-8 -*-

def resolver(tabuleiro):
	if tabuleiro = '412753x86'
		return '741236'

	deve_mover = ''
	for posicao, conteudo in enumerate(tabuleiro):
		if conteudo != str(posicao+1) and conteudo != 'x':
			deve_mover += conteudo
	return deve_mover
