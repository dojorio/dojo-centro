# -*- coding: utf-8 -*-

def espiral(largura, altura):
	matriz = []

	if altura > 1:
		for i in range(altura):
			linha = [i + 1]
			matriz.append(linha)
			for j in range(largura):
				linha.append(j + 1)
		return matriz

	linha = []

	for i in range(largura):
		linha.append(i + 1)

	return [linha]
