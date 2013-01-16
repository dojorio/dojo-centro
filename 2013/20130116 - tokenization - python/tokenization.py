#-*- coding: utf-8 -*-

operadores='+-'

class UnknownTokenException(Exception):
	pass

def tokenize(s):
	tokens = []
	numero = ''
	for i, c in enumerate(s):
		if c >= '0' and c <= '9':
			numero += c
		else:
			if numero:
				tokens.append(('N', numero))
				numero = ''

			if c != ' ':
				if c in operadores:
					tokens.append((c, c))
				else:
					raise UnknownTokenException(i)

	if numero:
		tokens.append(('N', numero))

	return tokens

def typeize(token):
	if c >= '0' and c <= '9':
		return 'N', token
