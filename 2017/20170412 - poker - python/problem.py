#!/usr/bin/env python
# -*- coding: utf-8 -*-

def eh_uma_dupla(valores):
	if len(valores) == 1:
		return True
	if valores[0] == valores[1]:
		return True


def poker(j1, j2):
	valores1, valores2 = j1[::3], j2[::3]
	if len(valores1) == 1:
		if max(valores1) > max(valores2):
			return 1
			
	if eh_uma_dupla(valores1):
		return 1
	if eh_uma_dupla(valores2):
		return 2
	return 2