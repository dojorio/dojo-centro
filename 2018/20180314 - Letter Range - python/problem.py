#!/usr/bin/env python
# -*- coding: utf-8 -*-

def letter_range(str):
	if str == '':
		return []
	if len(str) > 1 and str[0] != str[1]:
		return ['a:b']
	return [str[0]+":"+str[0]]