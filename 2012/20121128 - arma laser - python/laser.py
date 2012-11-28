#coding: utf-8

linha = lambda soldado: soldado[0]
coluna = lambda soldado: soldado[1]

def laser(soldados):
	tiros = len(soldados)

	if tiros < 2:
		return tiros

	for soldado1, soldado2 in zip(soldados, soldados[1:]):
		if linha(soldado1) == linha(soldado2):
			tiros -= 1

		if coluna(soldado1) == coluna(soldado2):
			tiros -= 1


	return tiros


