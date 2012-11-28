#coding: utf-8
linha = lambda soldado: soldado[0]
coluna = lambda soldado: soldado[1]

def laser(soldados):
	same_column = set(map(coluna, soldados))
	same_line = set(map(linha, soldados))

	return min(len(same_column), len(same_line))