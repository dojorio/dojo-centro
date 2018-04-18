#!/usr/bin/env python
# -*- coding: utf-8 -*-

def pascal_triangle(n):
	"""
		input = n
		output = [[1], 
				[1, 1], 
			   [1, 2, 1]]
	"""
	triangle = []
	last_row = None
	for i in range(n):
		if i == 0:
			triangle.append([1])
		if i == 1:
			last_row = [1, 1]
			triangle.append(last_row)
		if i == 2:
			last_row = [1, sum(last_row), 1]
			triangle.append(last_row)
		if i == 3:
			new_number = last_row[0] + last_row[1]
			triangle.append([1, new_number, new_number, 1])
	return triangle