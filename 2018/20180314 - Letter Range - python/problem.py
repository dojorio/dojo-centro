#!/usr/bin/env python
# -*- coding: utf-8 -*-

def letter_range(str):
	if str == '':
		return []
	if len(str) == 1:
		return [str+":"+str]
	str = sorted(str)
	if len(str) == 2 and (ord(str[1]) - ord(str[0]) == 1):		
		return [str[0]+":"+str[1]]

	elif (ord(str[1]) - ord(str[0]) > 1):
		return [str[0]+":"+str[0], str[1]+":"+str[1]]

	