#!/usr/bin/env python
# -*- coding: utf-8 -*-

def escudo_antibruxa(criancas, sal):
	BRUXA_WINS = 'BRUXA WINS'
	KIDS_WIN   = 'KIDS WIN'
	if sal >= 8 and len(criancas) == 1:		
		return KIDS_WIN
	return BRUXA_WINS