# -*- coding: utf-8 -*-

def directions(streets):
	degree = {}

	for a, b in streets:
		degree[a] = degree.get(a, 0) + 1
		degree[b] = degree.get(b, 0) + 1

	return len([value for value in degree.values() if value >= 2])
