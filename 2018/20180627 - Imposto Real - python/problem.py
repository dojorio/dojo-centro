#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import ceil

def traveled_distance(capacity, debits, roads):
	traveled = 0

	for road in roads:
		debit_index = max(road[0], road[1]) - 1
		road_length = road[2]
		city_debt = debits[debit_index]

		traveled += road_length * ceil(city_debt/capacity) * 2

	return traveled 
