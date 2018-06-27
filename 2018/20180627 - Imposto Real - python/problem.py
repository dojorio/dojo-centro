#!/usr/bin/env python
# -*- coding: utf-8 -*-

def traveled_distance(capacity, debits, roads):
	if debits[1] != 1:
		return roads[0][2] * debits[1] * 2 
	if debits[1]:
		return roads[0][2] * 2
	else:
		return 0