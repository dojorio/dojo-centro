# -*- coding: utf-8 -*-

def andar_pra_frente(largura):
	linha = []

	for i in range(largura):
		linha.append(i + 1)
	return linha

def andar_pra_baixo(altura):
	coluna = []
	for i in range(altura):
		linha = [i + 1]
		coluna.append(linha)

	return coluna

def espiral(largura, altura):
	matriz = []
	if largura == 2 and altura == 2:
		return [[1,2],[4,3]]


	for i in range(altura):
		linha = andar_pra_frente(largura)
		matriz.append(linha)
	return matriz


	if altura > 1:
		return andar_pra_baixo(altura)
	return [andar_pra_frente(largura)]
