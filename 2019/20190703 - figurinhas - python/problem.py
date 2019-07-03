#!/usr/bin/env python
# -*- coding: utf-8 -*-

def maior_pilha(pilha_1, pilha_2):
	if max(pilha_1, pilha_2) % min(pilha_1, pilha_2) == 0:
		return min(pilha_1, pilha_2)

	else:
		return 1