# -*- coding: utf-8 -*-

def skyline(predios):
	if not predios:
		return []
	else:
		result = []
		for predio in predios:
			result += [(predio[0], predio[1]), (predio[2], 0)]

		return result
