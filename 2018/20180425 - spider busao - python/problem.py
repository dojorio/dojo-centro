#!/usr/bin/env python
# -*- coding: utf-8 -*-

def spider_walk(riocard, bus_graph):
	ARRIVED = "Chegou!"
	NOT_ARRIVED = "Não Chegou!"

	edge_price = bus_graph[0][2]

	if edge_price > riocard:
		return NOT_ARRIVED

	return ARRIVED