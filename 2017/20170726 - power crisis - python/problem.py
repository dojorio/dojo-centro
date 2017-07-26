#!/usr/bin/env python
# -*- coding: utf-8 -*-

def power_crisis(n):
	#if n == 13:
	#	 return 1
	ms = [1,5,7,8,9,10,11,13,14] + list(range(15, 85))

	for index, m in enumerate(ms):
		l = list(range(1, n+1))
		pos = 0
		while len(l) > 1:
			l.pop(pos)
			pos = (pos + m - 1) % len(l)
		if l[0] == 13:
			print(index+1)
			return m
