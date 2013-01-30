#-*- coding: utf-8 -*-

def formiga(tempo):
	posicoes = {
		0: (0, 0),
		1: (0, 1),
		2: (1, 1),
		3: (1, 0),
		4: (2, 0),
		5: (2, 1)
	}

	return posicoes[tempo]