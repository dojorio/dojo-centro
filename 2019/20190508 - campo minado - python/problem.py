#!/usr/bin/env python
# -*- coding: utf-8 -*-

def gera_campo(campo):
	resultado = []

	for linha in campo:
		lista = list(linha.replace('.','0'))

		while '*' in lista:
			indice = lista.index('*')

			if indice > 0:
				lista[indice - 1] = str(int(lista[indice - 1]) + 1)
			if indice < len(lista) - 1:
				lista[indice + 1] = str(int(lista[indice + 1]) + 1)

			lista[indice] = '9'

		resultado.append(''.join(lista).replace('9', '*'))

	return resultado
	