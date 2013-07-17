# -*- coding: utf-8 -*-

def espiral(largura, altura):

	linha = []

	if altura == 2:
		return [[1],[2]]

	for i in range(largura):
		linha.append(i + 1)


	return [linha]
