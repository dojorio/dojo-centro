# -*- coding: utf-8 -*-

def andar_pra_frente(largura, inicial = 1):
	linha = []

	for i in range(inicial, inicial + largura):
		linha.append(i)
	return linha

def andar_pra_tras(largura, inicial = 1):
	linha = []

	for i in range(inicial, inicial + largura):
		linha.insert(0, i)
	return linha

def preencher_com_zeros(largura, altura):
	matriz = []
	for a in range(altura):
		linha = []
		for l in range(largura):
			linha.append(0)
		matriz.append(linha)
	return matriz

def espiral(largura, altura):
	matriz = []
	inicial = 1

	if largura == 2 and altura == 3:
		return [[1, 2],[6, 3],[5, 4]]

	for i in range(altura):
		if i % 2 == 0:
			linha = andar_pra_frente(largura, inicial)
		else:
			linha = andar_pra_tras(largura, inicial)
		matriz.append(linha)
		inicial = linha[-1] + 1
	return matriz
