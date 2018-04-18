#!/usr/bin/env python
# -*- coding: utf-8 -*-

def new_line (old):
	pri = [0] + old # [0, 1, 2, 1]
	sec = old + [0] # [1, 2, 1, 0]
	return [v + sec[k] for k, v in enumerate(pri)] # [1, 3, 3, 1]

def pascal_triangle(n):
	"""
		input = n # 3
		output = [[1], 
				[1, 1], 
			   [1, 2, 1]]
	"""
	triangle = []
	last_row = None
	for i in range(n):
		if i == 0:
			last_row = [1]
			triangle.append(last_row)
		else:
			triangle.append(new_line(last_row))


	return triangle