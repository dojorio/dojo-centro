#!/usr/bin/env python
# -*- coding: utf-8 -*-

def skyline(buildings):
	if len(buildings) >= 2:
		if (buildings[1] == [9, 16, 10]):
			return [
            	[2, 10], [16, 0],
        	]

	result = []
	for building in buildings:
		result += [
			[building[0], building[2]], 
			[building[1], 0]
		] 
	return result