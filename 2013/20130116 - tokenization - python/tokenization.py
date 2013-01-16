#-*- coding: utf-8 -*-

def tokenize(s):
	if s in '+-':
		kind = s
	else:
		kind = 'N'
	return [(kind, s)]