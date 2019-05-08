#!/usr/bin/env python
# -*- coding: utf-8 -*-

def gera_campo(campo):


	if '*' in campo[0]:
		lista = campo[0].split()
		print(lista)
		indice = lista.index('*')
		if indice > 0:
			lista[indice-1] = '1'
		if indice < len(lista)-1:
			lista[indice+1] = '1'
		campo[0] = join(lista)

		
	return [campo[0].replace('.', '0')]
	