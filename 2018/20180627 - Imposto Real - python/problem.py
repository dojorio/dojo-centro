#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import ceil

def traveled_distance(capacity, debits, roads):
	traveled = 0

	for city_index, road in enumerate(roads):
		traveled += road[2] * ceil(debits[city_index + 1]/capacity) * 2

	return traveled 
