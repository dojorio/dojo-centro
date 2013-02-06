#-*- coding: utf-8 -*-

#2+3+4

#2
#('+', 2, 3)
#('+', ('+', 2, 3), 4)

def parse(tokens):
	resultado = int(tokens[0][1])

	for i in range(1, len(tokens), 2):
		resultado = (tokens[i][0], resultado, int(tokens[i+1][1]))

	return resultado