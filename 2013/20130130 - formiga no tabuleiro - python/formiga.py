#-*- coding: utf-8 -*-

from math import *

def formiga(tempo):
	tempo_raiz = sqrt(tempo)

	tempo_raiz_int = int(tempo_raiz)
	medio = (tempo_raiz_int + 1)*tempo_raiz_int
	max(tempo, medio)

	if tempo_raiz_int % 2 == 0:
		return (tempo_raiz_int-max(medio-tempo, 0), tempo_raiz_int-max(tempo-medio, 0))
	else:
		return (tempo_raiz_int-max(tempo-medio, 0), tempo_raiz_int-max(medio-tempo, 0))