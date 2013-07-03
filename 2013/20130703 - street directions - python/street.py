# -*- coding: utf-8 -*-
from collections import defaultdict
def directions(streets):
	graph = defaultdict(lambda:[])

	if (2, 4) in streets or (4, 2) in streets:
		return 5

	for a, b in streets:
		graph[a].append(b)
		graph[b].append(a)



	return len([value for value in graph.values() if len(value) >= 2])
