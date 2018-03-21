#!/usr/bin/env python
# -*- coding: utf-8 -*-

BRUXA_WINS = 'BRUXA WINS'
KIDS_WIN   = 'KIDS WIN'

def escudo_antibruxa(criancas, sal):
	kids_distance_x = 0
	number_of_kids = len(criancas) 
		
	if number_of_kids == 1:	
		if sal >= 8:
			return KIDS_WIN
	elif number_of_kids == 2:
		kids_distance_x = abs(criancas[1][0] - criancas[0][0])
		kids_distance_y = abs(criancas[0][1] - criancas[0][0])
		needed = 16 if kids_distance_x >= 4 else (8 + kids_distance_x*2)
		if (sal >= needed):
			return KIDS_WIN
	return BRUXA_WINS

