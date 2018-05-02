#!/usr/bin/env python
# -*- coding: utf-8 -*-

def skyline(buildings):
	# if len(buildings) == 1:
	# 	return [
	#         [buildings[0][0], buildings[0][2]], 
	#         [buildings[0][1], 0],
	#     ]
	# elif len(buildings) == 2:
	# 	return [
	#         [buildings[0][0], buildings[0][2]], 
	#         [buildings[0][1], 0],

	#         [buildings[1][0], buildings[1][2]], 
	#         [buildings[1][1], 0],
	#     ]
	# elif len(buildings) == 3:
	result = []
	for building in buildings:
		result += [building[0], building[2], building[1], 0] 
	return result