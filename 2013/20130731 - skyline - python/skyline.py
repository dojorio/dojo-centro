# -*- coding: utf-8 -*-

def skyline(buildings):
	result = [(el[0], el[1]) for el in buildings]
	result.append((buildings[-1][1], 0))
	return result
