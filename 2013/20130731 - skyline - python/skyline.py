# -*- coding: utf-8 -*-

def skyline(buildings):
	if buildings == []:
		return []

	result = []
	altura_anterior = -1
	for predio in buildings:
		inicio, altura, fim = predio

		if altura != altura_anterior:
			result.append((inicio, altura))

		altura_anterior = altura

	result.append((buildings[-1][-1], 0))
	return result
