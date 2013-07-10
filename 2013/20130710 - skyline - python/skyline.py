# -*- coding: utf-8 -*-

def skyline(predios):
	if not predios:
		return []
	else:
		result = []
		#x_anterior = -1

		for predio in predios:
			#if predio[0] == x_anterior:
			#	del result[-1]
			#else:
				result += [(predio[0], predio[1]), (predio[2], 0)]
			#	x_anterior = predio[2]

		return result
