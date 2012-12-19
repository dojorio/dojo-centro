#coding: utf-8
from math import sqrt

def noel(criancas):
	crianca_mais_distante = max(criancas)
	return sqrt(crianca_mais_distante[0]**2 + 
				crianca_mais_distante[1]**2)

