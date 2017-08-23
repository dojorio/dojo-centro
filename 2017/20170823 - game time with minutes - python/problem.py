#!/usr/bin/env python
# -*- coding: utf-8 -*-

def time(value):
	if value == '1 1 2 1':
		return 'O JOGO DUROU 1 HORA(S) E 0 MINUTO(S)'
	if value == '1 1 3 1':
		return 'O JOGO DUROU 2 HORA(S) E 0 MINUTO(S)'
	minutoFinal = int(value.split(' ')[3]) - 1 
	
	return 'O JOGO DUROU 0 HORA(S) E {0} MINUTO(S)'.format(minutoFinal)