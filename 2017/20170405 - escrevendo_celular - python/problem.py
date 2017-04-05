#!/usr/bin/env python
# -*- coding: utf-8 -*-

letra_x_numero = (('A','B','C'),
				  ('D','E','F'))


def teclado(palavra):
	numero = ""

	for letra in palavra:
		numero += str(letra_x_numero[letra])
	return int(numero)