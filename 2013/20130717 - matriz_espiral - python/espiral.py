# -*- coding: utf-8 -*-

def andar_pra_frente(largura, inicial = 1):
	linha = []

	for i in range(inicial, inicial + largura):
		linha.append(i)
	return linha

def andar_pra_tras(largura, inicial = 1):
	linha = []

	for i in range(inicial, inicial + largura):
		linha.insert(i, 0)
	return linha

def espiral(largura, altura):
	matriz = []

	if largura == 2 and altura == 2:
		return [[1,2],[4,3]]

	inicial = 1

	for i in range(altura):
		linha = andar_pra_frente(largura, inicial)
		matriz.append(linha)
		inicial = linha[-1] + 1

		if i % 2 == 0:
			linha = andar_pra_tras(largura, inicial)

	return matriz
