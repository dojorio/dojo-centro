#-*- coding: utf-8 -*-

def tokenize(s):
	if len(s) > 1:
		return [('N', '1'),('+', '+'),('N', '1')]
	else:
		if s in '+-':
			kind = s
		else:
			kind = 'N'
		return [(kind, s)]