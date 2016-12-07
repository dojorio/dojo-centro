#!/usr/bin/env python
# -*- coding: utf-8 -*-
def CriaMatriz(navios,tiros):
	lista = []
	
	if tiros[0] in navios[0]:
		return [(tiros[0],)]

	if len(navios) > 3:
		if tiros[0] in navios[1]:
			return [(tiros[0],)]

	return []