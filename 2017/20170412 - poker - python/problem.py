#!/usr/bin/env python
# -*- coding: utf-8 -*-

def eh_uma_dupla(valores):
	if valores[0] == valores[1]:
		return True


def poker(jogador1, jogador2):
	valores1, valores2 = jogador1[::3], jogador2[::3]

	if len(valores1) == 1:
		if max(valores1) > max(valores2):
			return 1
		return 2

	if eh_uma_dupla(valores1) and eh_uma_dupla(valores2):
		if max(valores1) > max(valores2):
			return 1
		else:
			return 2
	else:
		if eh_uma_dupla(valores1):
			return 1

		if eh_uma_dupla(valores2):
			return 2
			
	if max(valores1) > max(valores2):
		return 1
	else:
		return 2