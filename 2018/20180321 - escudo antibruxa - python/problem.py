#!/usr/bin/env python
# -*- coding: utf-8 -*-

def escudo_antibruxa(criancas, sal):
	BRUXA_WINS = 'BRUXA WINS'
	KIDS_WIN   = 'KIDS WIN'

	return KIDS_WIN if sal == 8 or sal == 9 or sal == 10 else BRUXA_WINS