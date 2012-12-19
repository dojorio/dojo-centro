#coding: utf-8
from math import sqrt
from functools import partial

def distancia(a, b):
	return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def ponto_mais_proximo(ponto, pontos_restantes):
	return min(distancia(ponto,ponto_da_vez) for ponto_da_vez in \
		 pontos_restantes)


ORIGEM = (0,0)

def noel(criancas):
	posicao = ORIGEM
	distancia_percorrida = 0
	distancia_separando = 0

	criancas.sort(key=partial(distancia, ORIGEM))

	visitadas = [ORIGEM]
	que_faltam = criancas

	for crianca in criancas:
		distancia_percorrida += distancia(posicao, crianca)
		distancia_separando += distancia(ORIGEM, crianca)
		visitadas.append(crianca)
		que_faltam = criancas - visitadas
		posicao = crianca

	
	return min(distancia_percorrida, distancia_separando)
