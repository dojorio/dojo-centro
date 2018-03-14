#!/usr/bin/env python
# -*- coding: utf-8 -*-

def letter_range(str):
	if str == '':
		return []

	str = sorted(set(str.replace(" ", "")))
	if len(str) == 2:		
		if (ord(str[1]) - ord(str[0]) == 1):
			return [str[0]+":"+str[1]]

		else:
			return [str[0]+":"+str[0], str[1]+":"+str[1]]

	return [str[0]+":"+str[0]]