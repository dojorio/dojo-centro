#-*- coding: utf-8 -*-

from math import *

def formiga(tempo):
	x = 0
	y = 0

	posicoes = {
		0: (0, 0),
		1: (1, 0), # ( 1,  0)
		2: (1, 1), # ( 0,  1)
		3: (0, 1), # (-1,  0)
		4: (0, 2), # ( 0,  1)
		5: (1, 2), # ( 1,  0)
		6: (2, 2), # ( 1,  0)
		7: (2, 1), # ( 0, -1)
		8: (2, 0), # ( 0, -1)
	}

	tempo_raiz = sqrt(tempo)

	# Tá no eixo Y
	if tempo_raiz % 2 == 0:
		return (0, int(tempo_raiz))

	# Tá no eixo X
	if tempo_raiz % 2 == 1:
		return (int(tempo_raiz), 0)

	tempo_raiz_int = int(tempo_raiz)
	medio = (tempo_raiz_int + 1)*tempo_raiz_int

	# Tá na quina
	if tempo == medio:
		return (tempo_raiz_int, tempo_raiz_int)

	if tempo_raiz_int % 2 == 0:
		if tempo > medio:
			return (tempo_raiz_int, tempo_raiz_int-(tempo-medio))
		else:
			return (tempo_raiz_int-(medio-tempo), tempo_raiz_int)
	else:
		if tempo > medio:
			return (tempo_raiz_int, tempo_raiz_int-(tempo-medio))
		else:
			return (tempo_raiz_int-(medio-tempo), tempo_raiz_int)