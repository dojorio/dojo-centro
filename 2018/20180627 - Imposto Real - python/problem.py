#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import ceil

def traveled_distance(capacity, debits, roads):
	traveled = 0

	for road in roads:
		debit_index = max(road[0], road[1]) - 1
		traveled += road[2] * ceil(debits[debit_index]/capacity) * 2

	return traveled 
