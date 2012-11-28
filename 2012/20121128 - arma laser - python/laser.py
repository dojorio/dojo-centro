#coding: utf-8
from itertools import groupby, chain

linha = lambda soldado: soldado[0]
coluna = lambda soldado: soldado[1]

def laser(soldados):
	colunas = groupby(soldados, coluna)
	linhas = groupby(soldados, linha)

	tudao = colunas + linha

	for col, soldados_coluna in colunas:



	qtd_soldados_em_colunas = qtd_soldados_na_coluna(coluna, soldados)
	qtd_soldados_em_linas qtd_soldados_na_linha(linha, soldados)

	same_column = set(map(coluna, soldados))
	same_line = set(map(linha, soldados))

	return min(len(same_column), len(same_line))