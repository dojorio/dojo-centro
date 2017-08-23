#!/usr/bin/env python
# -*- coding: utf-8 -*-

def time(value):
	minutoFinal = int(value.split(' ')[3]) - 1 
	
	return 'O JOGO DUROU 0 HORA(S) E {0} MINUTO(S)'.format(minutoFinal)