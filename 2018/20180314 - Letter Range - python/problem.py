#!/usr/bin/env python
# -*- coding: utf-8 -*-

def letter_range(str):
	if str == '':
		return []

	if len(str) == 2:
		str = sorted(str)
		return [str[0]+":"+str[1]]

	return [str[0]+":"+str[0]]