#!/usr/bin/env python
# -*- coding: utf-8 -*-

def quantidade_buracos(texto):
	zero_buraco = ['C','E','F','G']
	if texto == 'B':
		return 2
	for letra in range(zero_buraco):
		if texto == zero_buraco[letra]:
			return 0
	return 1