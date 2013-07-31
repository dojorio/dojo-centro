# -*- coding: utf-8 -*-

def skyline(buildings):
	if buildings == []:
		return []
	inicio, altura, fim = buildings[0]
	return [(inicio, altura), (fim, 0)]
