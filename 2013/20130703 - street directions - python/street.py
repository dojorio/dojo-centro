# -*- coding: utf-8 -*-
from collections import defaultdict

#Depth-First Search
def dfs(graph, begin, end, visited, twoway, level):
	visited[end] = level

	cycle_size = 0
	for other in graph[end]:
		if other not in visited:
			cycle_size = max(cycle_size, dfs(graph, end, other, visited, twoway, level + 1))
		elif other != begin:
			cycle_size = max(cycle_size, level - visited[other])

	if cycle_size <= 0:
		twoway.append((begin, end))

	return cycle_size - 1



def directions(streets):
	graph = defaultdict(lambda:[])

	for a, b in streets:
		graph[a].append(b)
		graph[b].append(a)

	twoway = []
	dfs(graph, None, 1, {}, twoway, 0)
	return len(streets) - (len(twoway) - 1)
