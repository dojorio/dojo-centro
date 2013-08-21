# -*- coding: utf-8 -*-

def votacao(gatos, caes, votos):
	if len(votos) == 2:
		if votos[0][1] == votos[1][0] or votos[0][0] == votos[1][1]:
			return 1
	return len(votos)
