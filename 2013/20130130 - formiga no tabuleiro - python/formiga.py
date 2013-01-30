#-*- coding: utf-8 -*-
from math import sqrt

def formiga(tempo):
	raiz_tempo = int(sqrt(tempo))
	quina_mais_proxima = raiz_tempo * (raiz_tempo + 1)

	if raiz_tempo % 2:
		distancia_quina = tempo - quina_mais_proxima
	else:
		distancia_quina = quina_mais_proxima - tempo

	x = raiz_tempo - max( distancia_quina, 0)
	y = raiz_tempo - max(-distancia_quina, 0)
	
	return (x, y)