#coding: utf-8
from math import sqrt

def distancia(a, b):
	return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)



def noel(criancas):
	posicao = (0, 0)
	distancia_percorrida = 0

	criancas.sort(key=lambda crianca: distancia( (0,0), crianca ))

	for crianca in criancas:
		distancia_percorrida += distancia(posicao, crianca)
		posicao = crianca
	
	return distancia_percorrida
