#!/usr/bin/env python
# -*- coding: utf-8 -*-

def escudo_antibruxa(criancas, sal):
	BRUXA_WINS = 'BRUXA WINS'
	KIDS_WIN   = 'KIDS WIN'
	if sal >= 8 and len(criancas) == 1:	
		return KIDS_WIN
	elif sal >= 10 and len(criancas) == 2 and (criancas[1][0] - criancas[0][0] == 1):
		return KIDS_WIN
	return BRUXA_WINS
