#!/usr/bin/env python
# -*- coding: utf-8 -*-

def spider_walk(riocard, bus_graph):
	ARRIVED = "Chegou!"
	NOT_ARRIVED = "Não Chegou!"

	if (bus_graph[0][2] > 10 and
		riocard != 15):
		return NOT_ARRIVED

	return ARRIVED