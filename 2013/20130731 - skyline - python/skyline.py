# -*- coding: utf-8 -*-

def skyline(buildings):
	if buildings == []:
		return []

	result = []
	for predio in buildings:
		inicio, altura, fim = predio
		result += [(inicio, altura), (fim, 0)]
	result.sort()

	result2 = []
	altura_anterior = 0
	for cota in result:
		inicio, altura = cota
		if altura > altura_anterior:
			result2.append(cota)
	return result2

	altura_anterior = -1
	fim_anterior = -1
	for predio in buildings:
		inicio, altura, fim = predio

		if altura != altura_anterior:
			if altura < altura_anterior:
				inicio = fim_anterior

			result.append((inicio, altura))


		fim_anterior = fim
		altura_anterior = altura

	ultimo_predio = buildings[-1]
	result.append((ultimo_predio[-1], 0))
	return result
