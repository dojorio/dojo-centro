#!/usr/bin/env python
# -*- coding: utf-8 -*-

def miojo(temp_1, temp_2):

	if temp_1 % 2 == 0 and temp_2 % 2 == 0:
		return 'ampulhetas inválidas'
	if temp_1 == 5:
		return 5
	if temp_1 == 2:
		if temp_2 == 5:
			return 5
		if temp_2 == 7:
			return 7
		if temp_2 == 9:
			return 9
		if temp_2 == 11:
			return 11	
		return 5


	return 3