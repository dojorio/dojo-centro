#!/usr/bin/env python
# -*- coding: utf-8 -*-
def CriaMatriz(navios,tiros):
	lista = []
	for i in navios:
		for a in i:
			if tiros[a]:
				lista.append(a)
	return lista
	
	if tiros[0] in navios[0]:
		return [(tiros[0],)]

	if tiros[0] in 'b1':
		return [(tiros[0],)]

	return []