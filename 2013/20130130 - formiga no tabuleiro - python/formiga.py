#-*- coding: utf-8 -*-

from math import *

def formiga(tempo):
	
	raiz_tempo = int(sqrt(tempo))
	quina = (raiz_tempo + 1)*raiz_tempo

	x, y = raiz_tempo-max(quina-tempo, 0), raiz_tempo-max(tempo-quina, 0)
	
	if raiz_tempo % 2 != 0:
		y, x = x, y
	
	return (x, y)