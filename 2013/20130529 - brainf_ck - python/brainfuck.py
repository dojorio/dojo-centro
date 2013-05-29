#-*- coding: utf-8 -*-

def brainfuck(programa, entrada):
	mais = programa.count('+')
	menos = programa.count('-')
	pontos = programa.count('.')

	return chr(mais - menos) * pontos
