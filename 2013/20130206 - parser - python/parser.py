#-*- coding: utf-8 -*-

def parse(tokens):
	if len(tokens) == 1:
		return int(tokens[0][1])

	if ('+', '+') in tokens:
		op = ('+', '+')
	if ('-', '-') in tokens:
		op = ('-', '-')
	else:
		op = ('*', '*')

	index = (len(tokens)-1) - tokens[::-1].index(op)
	return (op[0], parse(tokens[:index]), parse(tokens[index+1:]))
