#!/usr/bin/env python
# -*- coding: utf-8 -*-

def quantidade_buracos(texto):
	if texto == 'B':
		return 2
	if texto == 'C' or texto == 'E' or texto == 'F' or texto == 'G':
		return 0
	return 1