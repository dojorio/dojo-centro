#!/usr/bin/env python
# -*- coding: utf-8 -*-

def power_crisis(n):
	#if  n == 13:
	#	return 1
	l = list (range(1, n+1))
	m = 1
	pos = 0
	while len(l) > 1:
		l.pop(pos)
		pos = pos + m - 1
	return l [0]
