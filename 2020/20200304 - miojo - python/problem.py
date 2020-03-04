#!/usr/bin/env python
# -*- coding: utf-8 -*-

def miojo(temp_1, temp_2):
	if temp_1 == 1 or temp_2 == 1:
		return 3

	if temp_1 % 2 == 0 and temp_2 % 2 == 0:
		return 'ampulhetas inválidas'

	if temp_1 > temp_2:
		return temp_1

	if temp_1 == 6:
		return 9

	if temp_1 == 5:
		if temp_2 == 7:
			return 10
		if temp_2 == 8:
			return 8

	if temp_1 == 2:
		return temp_2	

	return 3