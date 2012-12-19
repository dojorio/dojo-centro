#coding: utf-8
from math import sqrt

def distancia(a, b):
	return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)



def noel(criancas):
	posicao = (0, 0)
	distancia_percorrida = 0
	distancia_separando = 0

	criancas.sort(key=lambda crianca: distancia( (0,0), crianca ))

	for crianca in criancas:
		distancia_percorrida += distancia(posicao, crianca)
		distancia_separando += distancia((0,0), crianca)
		posicao = crianca
	
	return min(distancia_percorrida, distancia_separando)
