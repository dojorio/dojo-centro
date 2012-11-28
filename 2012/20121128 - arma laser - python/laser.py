#coding: utf-8

def laser(soldados):
	tiros = len(soldados)

	if tiros == 2 and soldados[0][0] == soldados[1][0]:
		tiros -= 1

	return tiros