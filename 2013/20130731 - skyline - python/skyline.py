# -*- coding: utf-8 -*-

def skyline(buildings):
	result = []
	if buildings == []:
		return result

	altura_anterior = -1
	fim_anterior = -1
	for inicio, altura, fim in buildings:

		if altura != altura_anterior:
			if altura < altura_anterior:
				inicio = fim_anterior

			predio_sobreposto = (
				(altura < altura_anterior) and (fim <= fim_anterior)
			)

			if not predio_sobreposto:
				result.append((inicio, altura))


		fim_anterior = fim
		altura_anterior = altura

	ultimo_predio = buildings[-1]
	result.append((ultimo_predio[-1], 0))

	return result
