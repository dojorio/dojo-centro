#-*- coding: utf-8 -*-

def brainfuck(programa, entrada):
	mais = programa.count('+')
	menos = programa.count('-')
	pontos = programa.count('.')
	celula = mais - menos
	if celula < 0:
		celula += 256
	return chr(celula) * pontos
