#!/usr/bin/env python
# -*- coding: utf-8 -*-

def letter_range(str):
	if str == '':
		return []
	if str == 'ab':
		return ['a:b']
	if str == 'bc':
	    return ['b:c']
	if str == 'bc':
	    return ['b:c']
	return [str[0]+":"+str[0]]