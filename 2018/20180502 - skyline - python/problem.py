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
	return [
        [buildings[0][0], buildings[0][2]],
        [buildings[0][1], 0],
        
        [buildings[1][0], buildings[1][2]],
        [buildings[1][1], 0],
        
        [buildings[2][0], buildings[2][2]],
        [buildings[2][1], 0],
    ]