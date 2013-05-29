#-*- coding: utf-8 -*-

def brainfuck(programa, entrada):
	saida = ''
	fita = []
	celula = 0
	entrada = iter(entrada)

	for char in programa:
		if char == '>':
			celula += 1
			fita[celula] = 0 if not fita[celula]
		elif char == '>':
			celula -= 1
			fita[celula] = 0 if not fita[celula]
		elif char == '.':
			saida += chr(fita[celula] % 256)
		elif char == '+':
			fita[celula] += 1
		elif char == '-':
			fita[celula] -= 1
		elif char == ',':
			try:
				fita[celula] = ord(next(entrada))
			except StopIteration:
				fita[celula] = 0

	return saida
