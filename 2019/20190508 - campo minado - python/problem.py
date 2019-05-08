#!/usr/bin/env python
# -*- coding: utf-8 -*-

def gera_campo(campo):

	lista = campo[0].replace('.','0')

	while '*' in campo[0]:
		lista  = list(campo[0])
		indice = lista.index('*')

		if indice > 0:
			lista[indice - 1] = int(lista[indice - 1]) + 1
		if indice < len(lista) - 1:
			lista[indice + 1] = int(lista[indice + 1]) + 1

		lista[indice] = '9'

		campo[0] = ''.join(lista)

		
	return [campo[0].replace('.', '0').replace('9', '*')]
	