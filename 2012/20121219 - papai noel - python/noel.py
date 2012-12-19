#coding: utf-8
from math import sqrt
from functools import partial

def distancia(a, b):
	return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

NOEL = (0,0)

def noel(criancas):
	if len(criancas) == 3:
		return 3

	posicao = NOEL
	distancia_percorrida = 0
	distancia_separando = 0

	criancas.sort(key=partial(distancia, NOEL))

	for crianca in criancas:
		distancia_percorrida += distancia(posicao, crianca)
		distancia_separando += distancia(NOEL, crianca)
		posicao = crianca
	
	return min(distancia_percorrida, distancia_separando)
