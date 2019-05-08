#!/usr/bin/env python
# -*- coding: utf-8 -*-

def gera_campo(campo):

	lista = campo[0].replace('.','0')

	while '*' in lista:
		lista  = list(lista)
		indice = lista.index('*')

		if indice > 0:
			lista[indice - 1] = str(int(lista[indice - 1]) + 1)
		if indice < len(lista) - 1:
			lista[indice + 1] = str(int(lista[indice + 1]) + 1)

		lista[indice] = '9'

		lista = ''.join(lista)

		
	return [lista.replace('.', '0').replace('9', '*')]
	