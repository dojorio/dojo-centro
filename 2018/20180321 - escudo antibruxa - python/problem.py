#!/usr/bin/env python
# -*- coding: utf-8 -*-

BRUXA_WINS = 'BRUXA WINS'
KIDS_WIN   = 'KIDS WIN'

def escudo_antibruxa(criancas, sal):
	kids_distance_x = 0
	number_of_kids = len(criancas) 
	if number_of_kids > 1:
		kids_distance_x = abs(criancas[1][0] - criancas[0][0])
	if sal >= 8 and number_of_kids == 1:	
		return KIDS_WIN
	elif (
		sal >= 10 and 
		number_of_kids == 2 and 
		(kids_distance_x == 1)
	) or (
		sal >= 12 and 
		number_of_kids == 2 and 
		(kids_distance_x == 2)
	):
		return KIDS_WIN
	elif sal >= 12:
		return KIDS_WIN
	return BRUXA_WINS

