#!/usr/bin/env python
# -*- coding: utf-8 -*-

def spider_walk(riocard, bus_graph):
	ARRIVED = "Chegou!"
	NOT_ARRIVED = "Não Chegou!"

	edge_price_1 = bus_graph[0][2]
	edge_price_2 = bus_graph[-1][2]

	if (
		edge_price_1 > riocard or
		edge_price_2 > riocard
	):
		return NOT_ARRIVED

	if (
		len(bus_graph) == 3
	):
		return NOT_ARRIVED

	return ARRIVED