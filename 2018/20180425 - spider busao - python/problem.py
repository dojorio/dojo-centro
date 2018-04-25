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
		start = edge[0]
		finish = edge[1]
		cost = edge[2]
		if graph.get(start, None) is None: 
			graph[start] = []
		graph[start].append((finish, cost))

	print(graph)

	accumulated_value = 0

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