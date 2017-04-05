#!/usr/bin/env python
# -*- coding: utf-8 -*-

letra_x_numero = {
	'A': 2,
	'B': 22,
	'C': 222,
	'D': 3,
}


def teclado(palavra):
	numero = ""
	for letra in palavra:
		numero += str(letra_x_numero[letra])
	return int(numero)