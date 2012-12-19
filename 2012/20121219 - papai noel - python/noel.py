#coding: utf-8
from math import sqrt

def noel(criancas):
	if len(criancas) == 2:
		return criancas[1][1]

	return sqrt(criancas[0][0]**2 + criancas[0][1]**2)
	