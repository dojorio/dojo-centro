#!/usr/bin/env python
# -*- coding: utf-8 -*-



def poker(j1, j2):
	valor1, naipe1 = j1[0], j1[1]
	valor2, naipe2 = j2[0], j2[1]
	if valor1 > valor2:
		return 1
	return 2