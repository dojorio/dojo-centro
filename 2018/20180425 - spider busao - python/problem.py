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

	stack = [
		(
			1, # current_node 
			0, # accumulated_value
			minascard # balance
		),
	]
	destination = max(graph.keys())

	while len(stack) > 0:
		current_node, accumulated_value, balance = stack.pop()

		for edge in graph[current_node]:
			current_edge_price = edge[1] - accumulated_value

			if current_edge_price <= balance:
				if edge[0] == destination:
					return ARRIVED

				stack.append(
					(
						edge[0],
						accumulated_value + current_edge_price,
						balance - current_edge_price,
					)
				)

	return NOT_ARRIVED