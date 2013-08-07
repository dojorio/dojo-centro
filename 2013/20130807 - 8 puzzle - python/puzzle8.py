# -*- coding: utf-8 -*-

def resolver(tabuleiro):
	if tabuleiro[2] == 'x':
		return '36'
	if tabuleiro[6] == 'x':
		return '78'
	if tabuleiro[-1] != 'x':
		return tabuleiro[-1]
	return ''
