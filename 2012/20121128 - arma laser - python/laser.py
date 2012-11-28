#coding: utf-8

linha = lambda soldado: soldado[0]
coluna = lambda soldado: soldado[1]

def laser(soldados):
	tiros = len(soldados)
	listMesmaColuna = []
	listMesmaLinha = []

	for soldado in soldados:
		listMesmaColuna.append(coluna(soldado))
		listMesmaLinha.append(linha(soldado))

	conjuntoLinhas = set(listMesmaLinha)
	conjuntoColunas = set(listMesmaColuna)

	return min(len(conjuntoColunas), len(conjuntoLinhas))