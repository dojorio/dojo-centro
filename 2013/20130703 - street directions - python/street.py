# -*- coding: utf-8 -*-
from collections import defaultdict
def dfs(graph, begin, end, visited, level=0):
	visited[end] = level

	result = 0
	for other in graph[end]:
		if other not in visited:
			result = max(result, dfs(graph, end, other, visited, level+1)-1)
		elif other != begin:
			result = max(result, level - visited[other] + 1)

	print (begin, end)

	return result



def directions(streets):
	graph = defaultdict(lambda:[])

	for a, b in streets:
		graph[a].append(b)
		graph[b].append(a)

	dfs(graph, None, streets[0][0], {})


	return len([value for value in graph.values() if len(value) >= 2])
