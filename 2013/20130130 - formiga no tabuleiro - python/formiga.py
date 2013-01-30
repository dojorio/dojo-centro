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

	if tempo_raiz % 2 == 0:
		return (0, int(tempo_raiz))

	if tempo_raiz % 2 == 1:
		return (int(tempo_raiz), 0)

	tempo_raiz_int = int(tempo_raiz)



	while tempo > 0:
		
		x += 1
		tempo -= 1

		while x != y and tempo > 0:
			y += 1
			tempo -= 1

		while x != 0 and tempo > 0:
			x -= 1
			tempo -= 1

		if tempo > 0:
			y += 1
			tempo -= 1

		while x != y and tempo > 0:
			x += 1
			tempo -= 1

		while y != 0 and tempo > 0:
			y -= 1
			tempo -= 1

	return (x, y)