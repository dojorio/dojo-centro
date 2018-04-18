#!/usr/bin/env python
# -*- coding: utf-8 -*-

#pattern = /<.*>/g

def count_diamonds(mine):
	#print(pattern.exec(mine))
	mine = mine.replace(".", "")
	count = 0
	while mine.count('<>') != 0:
		count += mine.count('<>')
		mine = mine.replace('<>','')

	return count

