#!/usr/bin/env python
# -*- coding: utf-8 -*-

def quantidade_buracos(texto):
	zero_buraco = "CEFGHIJKLMNSTUVWXYZ"
	if texto == 'B':
		return 2
#	for letra in zero_buraco:
#		if texto == letra:
	if texto in zero_buraco:
		return 0
	return 1