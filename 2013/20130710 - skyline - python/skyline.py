# -*- coding: utf-8 -*-

def skyline(predios):
	if not predios:
		return []
	else:
		result = []
		x_anterior = -1

		for x1, h, x2 in predios:
			if x1 == x_anterior:
				del result[-1]
			else:
				result.append((x1, h))

			x_anterior = x2
			result.append((x2, 0))

		return result
