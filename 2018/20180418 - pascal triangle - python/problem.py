#!/usr/bin/env python
# -*- coding: utf-8 -*-

def pascal_triangle(n):
	"""
		input = n
		output = [[1], [1, 1], [1, 2, 1]]
	"""
	triangle = []
	for n in range(n):
		print(n)
		if n == 1:
			triangle.append([1])
		if n == 2:
			triangle.append([1, 1])
	return triangle