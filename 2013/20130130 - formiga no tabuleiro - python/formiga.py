#-*- coding: utf-8 -*-

def formiga(tempo):
	posicoes = {
		0: (0, 0), # tempo /2 , 
		1: (0, 1),
		2: (1, 1),
		3: (1, 0),
		4: (2, 0),
		5: (2, 1),
		6: (2, 2),
		7: (1, 2)
		8: (0, 2)
	}
	#return (tempo/2, tempo%2)

	return posicoes[tempo]