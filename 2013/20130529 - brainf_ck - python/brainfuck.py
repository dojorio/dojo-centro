#-*- coding: utf-8 -*-
from collections import defaultdict

def brainfuck(programa, entrada):
	saida = ''
	fita = defaultdict(lambda: 0)
	celula = 0
	entrada = iter(entrada)

	for char in programa:
		if char == '>':
			celula += 1
		elif char == '<':
			celula -= 1
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
