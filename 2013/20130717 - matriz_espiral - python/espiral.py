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

def espiral(largura, altura):
	matriz = []
	inicial = 1

	for i in range(altura):
		if (i + 1) % 2 == 0:
			linha = andar_pra_tras(largura, inicial)
		else:
			linha = andar_pra_frente(largura, inicial)
		matriz.append(linha)
		inicial = linha[-1] + 1


	return matriz
