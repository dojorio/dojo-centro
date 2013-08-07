# -*- coding: utf-8 -*-

def resolver(tabuleiro):
	deve_mover = ''
	while tabuleiro != "x":
		posicao_do_x = tabuleiro.find('x')
		aonde_ta_quem_deveria_estar_na_posicao_do_x = tabuleiro.find(posicao_do_x)


	for posicao, conteudo in enumerate(tabuleiro):
		if conteudo != str(posicao+1) and conteudo != 'x':
			deve_mover += conteudo
	return deve_mover
