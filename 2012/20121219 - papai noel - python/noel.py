#coding: utf-8
from math import sqrt
from functools import partial

def distancia(a, b):
	return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

ORIGEM = (0,0)

def noel(criancas):
	posicao = ORIGEM
	distancia_percorrida = 0
	distancia_separando = 0

	criancas.sort(key=partial(distancia, ORIGEM))

	visitadas = []

	for crianca in criancas:
		distancia_percorrida += distancia(posicao, crianca)
		distancia_separando += distancia(ORIGEM, crianca)
		visitadas.append(crianca)
		posicao = crianca
	
	return min(distancia_percorrida, distancia_separando)
