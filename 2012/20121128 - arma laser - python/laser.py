#coding: utf-8

linha = lambda soldado: soldado[0]
coluna = lambda soldado: soldado[1]

def laser(soldados):
	tiros = len(soldados)

	if tiros == 2 and linha(soldados[0]) == linha(soldados[1]):
		tiros -= 1

	if coluna(soldados[0]) == coluna(soldados[1]):
		tiros -= 1

	return tiros


