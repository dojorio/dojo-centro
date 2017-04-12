#!/usr/bin/env python
# -*- coding: utf-8 -*-

def eh_um_par(valores):
	return len(valores) != 1 and valores[0] == valores[1]

def mao_maior(valores1, valores2):
	if max(valores1) > max(valores2):
		return 1
	return 2

def poker(jogador1, jogador2):
	valores1, valores2 = jogador1[::3], jogador2[::3]

	if eh_um_par(valores1):
		if eh_um_par(valores2):
			return mao_maior(valores1, valores2)
		else:
			return 1
	elif eh_um_par(valores2):
		return 2
	else:
		return mao_maior(valores1, valores2)
