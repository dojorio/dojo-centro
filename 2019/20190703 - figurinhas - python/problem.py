#!/usr/bin/env python
# -*- coding: utf-8 -*-

def maior_pilha(pilha_1, pilha_2):
	maior = max(pilha_1, pilha_2)
	menor = min(pilha_1, pilha_2)

	if maior % menor == 0:
		return menor

	aux = menor // 2

	while aux > 0:
		if maior % aux == 0 and menor % aux == 0:
			return aux
		else:
			aux -= 1
	
