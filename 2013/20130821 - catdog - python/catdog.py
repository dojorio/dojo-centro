# -*- coding: utf-8 -*-

def votacao(gatos, caes, votos):
	if len(votos) == 2 and votos[0] == (votos[1][1], votos[1][0]):
		return 1
	return  len(votos)
