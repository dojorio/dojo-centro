#!/usr/bin/env python
# -*- coding: utf-8 -*-
def CriaMatriz(a,b):
	
	if b[0] in a[0]:
		return [(b[0],)]

	if b[0] in 'b1':
		return [(b[0],)]

	return []