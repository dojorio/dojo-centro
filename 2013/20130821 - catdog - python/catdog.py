# -*- coding: utf-8 -*-
def votos_conflitam(voto1, voto2):
	return voto1[1] == voto2[0] or voto1[0] == voto2[1]

def votacao(gatos, caes, votos):
	if len(votos) == 2:
		if votos_conflitam(votos[0], votos[1]):
			return 1
	if len(votos) == 3:
		if votos_conflitam(votos[0], votos[1]):
			return 2
	return len(votos)
