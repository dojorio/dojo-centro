#!/usr/bin/env python
# -*- coding: utf-8 -*-

def spider_walk(riocard, bus_graph):
	ARRIVED = "Chegou!"
	NOT_ARRIVED = "Não Chegou!"

	edge_price_1 = bus_graph[0][2]
	edge_price_2 = bus_graph[-1][2]

	# construct graph
	graph = {}

	for edge in bus_graph:
		start, finish, cost = edge
		if graph.get(start, None) is None: 
			graph[start] = []
		graph[start].append((finish, cost))

	stack = [
		(
			1, # current_node 
			0, # accumulated_value
			riocard # balance
		),
	]

	while len(stack) > 0:
		current_node, accumulated_value, balance = stack.pop()

		for edge in graph[current_node]:
			current_edge_price = edge[1] - accumulated_value

			if current_edge_price <= balance:
				stack.append(
					(
						edge[0],
						accumulated_value + current_edge_price,
						balance - current_edge_price,
					)
				)



	if (
		edge_price_1 > riocard or
		edge_price_2 > riocard
	):
		return NOT_ARRIVED

	if len(bus_graph) == 3:
		edge_price_2 = bus_graph[1][2]
		if edge_price_2 > riocard:
			return NOT_ARRIVED

	return ARRIVED