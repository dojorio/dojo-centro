#coding: utf-8
from itertools import groupby
linha = lambda soldado: soldado[0]
coluna = lambda soldado: soldado[1]

def laser(soldados):
	if not soldados:
		return 0
	columns = set(map(coluna, soldados))
	lines = set(map(linha, soldados))
	
	qtd_col = [qtd_soldados_na_coluna(soldados, col), col for col in columns]
	qtd_lin = [qtd_soldados_na_linha(soldados, lin), lin for lin in lines]

	if max(qtd_col) > max(qtd_lin):
		soldados = filter(soldados, lambda soldado: coluna(soldado) != max(qtd_col)[1])
	else:
		soldados = filter(soldados, lambda soldado: linha(soldado) != max(qtd_lin)[1])

	return laser(soldados) + 1


def qtd_soldados_na_coluna(soldados, col):
	n = 0
	for soldado in soldados:
		if coluna(soldado) == col:
			n += 1
	return n

def qtd_soldados_na_linha(soldados, lin):
	n = 0
	for soldado in soldados:
		if linha(soldado) == lin:
			n += 1
	return n