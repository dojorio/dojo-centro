#!/usr/bin/env python
# -*- coding: utf-8 -*-

def maior_pilha(pilha_1, pilha_2):
	maior = max(pilha_1, pilha_2)
	menor = min(pilha_1, pilha_2)

	if maior % menor == 0:
		return menor
	elif maior % 2 == 0 and menor % 2 == 0:
		return 2
	elif maior % 3 == 0 and menor % 3 == 0:
		return 3
	
	return 1