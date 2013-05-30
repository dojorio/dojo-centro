#-*- coding: utf-8 -*-
from collections import defaultdict

def brainfuck(programa, entrada):
	saida = ''
	fita = defaultdict(lambda: 0)
	celula = 0
	entrada = iter(entrada)

	pc = 0

	while pc < len(programa):
		char = programa[pc]
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
		pc += 1

	return saida
