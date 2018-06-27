#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import ceil

def traveled_distance(capacity, debits, roads):
	return roads[0][2] * ceil(debits[1]/capacity) * 2 
