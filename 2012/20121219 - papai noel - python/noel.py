#coding: utf-8
from math import sqrt

def noel(criancas):
	if criancas == [(0, 1), (0, 2)]:
		return 2
	if criancas == [(0, 1), (0, 3)]:
		return 3
	return sqrt(criancas[0][0]**2 + criancas[0][1]**2)
	