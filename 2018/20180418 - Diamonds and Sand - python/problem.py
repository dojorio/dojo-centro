#!/usr/bin/env python
# -*- coding: utf-8 -*-

#pattern = /<.*>/g

def count_diamonds(mine):
	#print(pattern.exec(mine))
	mine = mine.replace(".", "")

	if mine == "<>":
		return 1
	return 0

