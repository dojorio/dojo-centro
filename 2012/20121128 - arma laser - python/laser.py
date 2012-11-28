#coding: utf-8
from itertools import groupby
linha = lambda soldado: soldado[0]
coluna = lambda soldado: soldado[1]

def laser(soldados):
	columns = set(map(coluna, soldados))
	lines = set(map(linha, soldados))
	
	#qtd_soldados_em_colunas = qtd_soldados_na_coluna(coluna, soldados)
	#qtd_soldados_em_linas = qtd_soldados_na_linha(linha, soldados)

	


	return min(len(columns), len(lines))

def qtd_soldados_na_coluna(soldados, col):
	n = 0
	for soldado in soldados:
		if coluna(soldado) == col:
			n += 1
	return n