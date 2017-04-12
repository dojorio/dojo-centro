#!/usr/bin/env python
# -*- coding: utf-8 -*-



def poker(j1, j2):
	valores1, valores2 = j1[::3], j2[::3]
	if max(valores1) > max(valores2):
		return 1
	return 2