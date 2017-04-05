#!/usr/bin/env python
# -*- coding: utf-8 -*-

letra_x_numero = (('A','B','C'),
				  ('D','E','F'))


def teclado(palavra):
	numero = ""

	for letra in palavra:

		for letra_index, letra_tuple in enumerate(letra_x_numero):
			try:
				posicao = letra_tuple.index(letra)
			except ValueError:
				continue
			numero += str(posicao + letra_index + 2)
		
	return int(numero)