# -*- coding: utf-8 -*-

def mover(tabuleiro, a, b):

	a, b = min(a, b), max(a, b)
	return tabuleiro[0:a]+tabuleiro[b]+tabuleiro[a+1:b]+tabuleiro[a]+tabuleiro[b:]

def resolver(tabuleiro):
	deve_mover = ''
	while tabuleiro[-1] != "x":
		posicao_do_x = tabuleiro.find('x')
		aonde_ta_quem_deveria_estar_na_posicao_do_x = tabuleiro.find(str(posicao_do_x + 1))
		deve_mover += str(posicao_do_x +1)
		tabuleiro = mover(tabuleiro, posicao_do_x, aonde_ta_quem_deveria_estar_na_posicao_do_x)

	return deve_mover

	for posicao, conteudo in enumerate(tabuleiro):
		if conteudo != str(posicao+1) and conteudo != 'x':
			deve_mover += conteudo
	return deve_mover
