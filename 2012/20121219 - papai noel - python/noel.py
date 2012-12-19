#coding: utf-8
from math import sqrt

def noel(criancas):
	if criancas[0][0] == criancas[0][1]:
		return sqrt(sum(criancas[0]))
	return sqrt(criancas[0][0]^2 + criancas[0][1]^2)
	