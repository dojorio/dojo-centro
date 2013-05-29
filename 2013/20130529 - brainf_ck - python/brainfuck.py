#-*- coding: utf-8 -*-

def brainfuck(programa, entrada):

	saida = ''
	indice_da_entrada = 0
	celula = 0

	for char in programa:
		if char == '.':
			saida += chr(celula % 256)
		elif char == '+':
			celula += 1
		elif char == '-':
			celula -= 1
		elif char == ',':
			celula = ord(next(entrada))
			indice_da_entrada += 1

	return saida
