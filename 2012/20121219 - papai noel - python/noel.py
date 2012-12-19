#coding: utf-8
from math import sqrt

def noel(criancas):
	if criancas[0] == criancas[1]:
		return sqrt(sum(criancas[0]))

	return max(criancas[0])