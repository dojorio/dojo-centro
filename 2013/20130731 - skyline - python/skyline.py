# -*- coding: utf-8 -*-

def skyline(buildings):
	if buildings == []:
		return []

	result = []
	altura_anterior = -1
	fim_anterior = -1
	for predio in buildings:
		inicio, altura, fim = predio

		if altura != altura_anterior:
			inicio = max(fim_anterior, inicio)

			result.append((inicio, altura))


		fim_anterior = fim
		altura_anterior = altura

	ultimo_predio = buildings[-1]
	result.append((ultimo_predio[-1], 0))
	return result
