#-*- coding: utf-8 -*-

def brainfuck(programa, entrada):

	saida = ''
	celula = 0

	for char in programa:
		if char == '.':
			saida += chr(celula % 256)
		elif char == '+':
			celula += 1
		elif char == '-':
			celula -= 1

	return saida
