#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import ceil

def traveled_distance(capacity, debits, roads):
	traveled = 0

	qty_of_cities = len(debits)
	costs =  [[None] * qty_of_cities] * qty_of_cities

	for road in roads:
		debit_index = max(road[0], road[1]) - 1
		road_length = road[2]
		city_debt = debits[debit_index]

		total_cost = road_length * ceil(city_debt/capacity) * 2

		costs[road[0] - 1][road[1] - 1] = total_cost
		costs[road[1] - 1][road[0] - 1] = total_cost

		if costs[0][road[1] - 1]:
			costs[0][road[0] - 1] = costs[0][road[1] - 1] + total_cost 

		# traveled += road_length * ceil(city_debt/capacity) * 2

	return sum(costs[0]) # traveled 
