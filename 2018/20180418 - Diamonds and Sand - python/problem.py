#!/usr/bin/env python
# -*- coding: utf-8 -*-

#pattern = /<.*>/g

def count_diamonds(mine):
	#print(pattern.exec(mine))
	mine = mine.replace(".", "")
	count_left = 0
	count_right = 0
	for ch in mine:
		if ch == '<':
			count_left += 1
		else:
			count_right += 1

		return min([count_left, count_right])


	return 0

