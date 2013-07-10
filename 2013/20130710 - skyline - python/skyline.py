# -*- coding: utf-8 -*-

def skyline(predios):
	if not predios:
		return []
	else:
		predio = predios[0]
		return [(predio[0], predio[1]), (predio[2], 0)]
