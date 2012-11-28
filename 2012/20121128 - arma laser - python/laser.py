#coding: utf-8
from itertools import groupby
linha = lambda soldado: soldado[0]
coluna = lambda soldado: soldado[1]

def laser(soldados):
	if not soldados:
		return 0
	columns = set(map(coluna, soldados))
	lines = set(map(linha, soldados))
	
	qtd_col = [(qtd_na(coluna, soldados, col), col, coluna) for col in columns]
	qtd_lin = [(qtd_na(linha, soldados, lin), lin, linha) for lin in lines]

	qtd, y, func = max(max(qtd_col), max(qtd_lin))

	soldados = filter(lambda soldado: func(soldado) != y, soldados)

	return min(laser(soldados) + 1, len(columns), len(lines))


def qtd_na(func, soldados, y):
	return len(filter(lambda x: func(x)==y, soldados))
	