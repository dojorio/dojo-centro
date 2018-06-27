#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import ceil

def traveled_distance(capacity, debits, roads):
	traveled = 0

	for road in roads:
		traveled += road[2] * ceil(debits[1]/capacity) * 2

	return traveled 
