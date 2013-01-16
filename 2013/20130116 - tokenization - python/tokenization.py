#-*- coding: utf-8 -*-

def tokenize(s):
	tokens = []
	numero = ''
	for c in s:
		if c >= '0' and c <= '9':
			numero += c
		else:
			if numero:
				tokens.append(('N', numero))
				numero = ''

			if c != ' ':				
				tokens.append((c, c))

	if numero:
		tokens.append(('N', numero))

	return tokens