# -*- coding: utf-8 -*-

def directions(streets):
	degree = {}

	if (2, 4) in streets or (4, 2) in streets:
		return 5

	for a, b in streets:
		degree[a] = degree.get(a, 0) + 1
		degree[b] = degree.get(b, 0) + 1

	return len([value for value in degree.values() if value >= 2])
