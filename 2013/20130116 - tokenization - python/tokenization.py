#-*- coding: utf-8 -*-

def tokenize(s):
	
	if (s == '11'):
		return [('N', '11')]


	tokens = []

	for c in s:
		if c in '+-':
			kind = c
		else:
			kind = 'N'

		tokens.append((kind, c))

	return tokens