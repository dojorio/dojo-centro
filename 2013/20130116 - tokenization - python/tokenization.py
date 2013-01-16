#-*- coding: utf-8 -*-

OPERATORS = '+-*/:()'

class UnknownTokenException(Exception):
	pass

def maybe_operator(tokens, i, c):
	if c != ' ':
		if c in OPERATORS:
			tokens.append((c, c))
		else:
			raise UnknownTokenException(i)

def maybe_number(tokens, number):
	if number:
		tokens.append(('N', number))
	return bool(number)

def tokenize(s):
	tokens = []
	number = ''
	for i, c in enumerate(s):
		if c >= '0' and c <= '9':
			number += c
			continue
		if maybe_number(tokens, number):
			number = ''
		maybe_operator(tokens, i, c)

	maybe_number(tokens, number)

	return tokens

def parse(tokens):
	saida = []
	saida.append(int(tokens[0][1]))

	for i in range (1, len(tokens), 2):



	if len(tokens) == 3:
		return [int(tokens[0][1]), int(tokens[2][1]), tokens[1][1]]

	return [int(tokens[0][1])]