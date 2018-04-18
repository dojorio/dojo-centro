#!/usr/bin/env python
# -*- coding: utf-8 -*-

#pattern = /<.*>/g

def count_diamonds(mine):
	#print(pattern.exec(mine))
	mine = mine.replace(".", "")
	diamonds = 0
	open_diamond = False
	for ch in mine:
		if ch == '<':
			open_diamond = True
		if ch == '>' and open_diamond:
			diamonds += 1
			open_diamond = False

	return diamonds

