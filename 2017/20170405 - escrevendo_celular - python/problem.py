#!/usr/bin/env python
# -*- coding: utf-8 -*-

letra_x_numero = ('ABC',
				  'DEF')


def teclado(palavra):
	numero = ""

	for letra in palavra:

		for letra_index, letra_tuple in enumerate(letra_x_numero):
			try:
				numero += str(letra_index+2) * (letra_tuple.index(letra) + 1)

			except ValueError:
				continue
		
	return int(numero)