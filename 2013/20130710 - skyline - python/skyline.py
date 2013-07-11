# -*- coding: utf-8 -*-

def skyline(predios):
	result = []
	x_anterior = -1
	x1_anterior = -1
	h_anterior = -1

	for x1, h, x2 in predios:
		if x2 < x_anterior:
			continue

		if x1 <= x_anterior:
			del result[-1]

		if x1 > x_anterior or h > h_anterior:
			result.append((x1, h))

		if x1 == x1_anterior and h > h_anterior:
			del result[0]

		x_anterior = x2
		x1_anterior = x1
		h_anterior = h
		result.append((x2, 0))

	return result
