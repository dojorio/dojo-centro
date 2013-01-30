#-*- coding: utf-8 -*-

def formiga(tempo):
	posicoes = {
		0: (0, 0), # tempo /2 , 
		1: (1, 0),
		2: (1, 1),
		3: (0, 1),
		4: (0, 2),
		5: (1, 2),
		6: (2, 2),
		7: (2, 1),
		8: (2, 0)
	}

	
	#return (tempo/2, tempo%2)

	return posicoes[tempo]