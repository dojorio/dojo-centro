#-*- coding: utf-8 -*-

def brainfuck(programa, entrada):
	saida = ''
	celula = 0
	entrada = iter(entrada)
	for char in programa:
		if char == '.':
			saida += chr(celula % 256)
		elif char == '+':
			celula += 1
		elif char == '-':
			celula -= 1
		elif char == ',':
			try:
				celula = ord(next(entrada))
			except StopIteration:
				celula = '\x00'


	return saida
