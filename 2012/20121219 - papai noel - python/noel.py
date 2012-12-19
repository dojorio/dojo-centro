#coding: utf-8
from math import sqrt
from functools import partial

def distancia(a, b):
	return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def menor_distancia(pontos_restantes, ponto):
	return min(distancia(ponto, x) for x in pontos_restantes)


ORIGEM = (0,0)

def noel(criancas):
	visitadas = [ORIGEM]
	que_faltam = criancas
	total = 0

	while len(que_faltam):
		mais_proxima = min(que_faltam, key=partial(menor_distancia, visitadas))
		
		total += menor_distancia(visitadas, mais_proxima)

		visitadas.append(mais_proxima)
		que_faltam.remove(mais_proxima)
	
	return total
