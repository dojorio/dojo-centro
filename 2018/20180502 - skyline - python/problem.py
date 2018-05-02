#!/usr/bin/env python
# -*- coding: utf-8 -*-

def skyline(buildings):
	result = []
	for building in buildings:
		result += [
			[building[0], building[2]], 
			[building[1], 0]
		] 
	return result