#!/usr/bin/env python
# -*- coding: utf-8 -*-

def power_crisis(n):
	#if  n == 13:
	#	return 1
	for m in [1,5,7,8,9,10,11,13,14]:
		l = list (range(1, n+1))
		pos = 0
		while len(l) > 1:
			l.pop(pos)
			pos = pos + m - 1
		if l[0] == 13:
			return m
