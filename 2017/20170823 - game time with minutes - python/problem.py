#!/usr/bin/env python
# -*- coding: utf-8 -*-

def time(value):
	minutoFinal = value.split(' ')
	minuto = 0
	if minutoFinal == 2:
		minuto = 1
	if minutoFinal == 3:
		minuto = 2
	if minutoFinal == 4:
		minuto = 3

	return 'O JOGO DUROU 0 HORA(S) E {0} MINUTO(S)'.format(minuto)