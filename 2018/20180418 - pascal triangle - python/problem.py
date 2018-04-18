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
	for i in range(n):
		print(i)
		if i == 0:
			triangle.append([1])
		if i == 1:
			triangle.append([1, 1])
		if i == 2:
			triangle.append([1, 2, 1])
	return triangle