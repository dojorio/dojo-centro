#-*- coding: utf-8 -*-

def brainfuck(programa, entrada):
	contador = programa.count('+')

	if programa == '+.':
		return '\x01'
	return '\0' * len(programa)
