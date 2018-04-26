#!/usr/bin/env python
# -*- coding: utf-8 -*-

def spider_walk(minascard, bus_graph):
	ARRIVED = "Chegou!"
	NOT_ARRIVED = "Não Chegou!"

	# construct graph
	graph = {}

	for edge in bus_graph:
		start, finish, cost = edge
		if graph.get(start, None) is None: 
			graph[start] = []
		if graph.get(finish, None) is None: 
			graph[finish] = []
		graph[start].append((finish, cost))

	stack = [1]
	destination = max(graph.keys())

	while len(stack) > 0:
		current_node = stack.pop()

		for edge in graph[current_node]:
			next_node, cost = edge
			if cost <= minascard:
				if next_node == destination:
					return ARRIVED

				stack.append(next_node)

	return NOT_ARRIVED