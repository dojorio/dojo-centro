# -*- coding: utf-8 -*-

def trocar(tabuleiro, a, b):
	a, b = min(a, b), max(a, b)
	return (tabuleiro[0:a]+
			tabuleiro[b]+
			tabuleiro[a+1:b]+
			tabuleiro[a]+
			tabuleiro[b+1:])

def resolver(tabuleiro):
	gabarito = "12345678x"
	deve_mover = ''

	for i in xrange(1000):
		de = tabuleiro.find('x')
		para = tabuleiro.find(str(de + 1))
		deve_mover += str(de + 1)
		tabuleiro = trocar(tabuleiro, de, para)
		if tabuleiro == gabarito: break

	return deve_mover
