# -*- coding: utf-8 -*-
def votos_conflitam(voto1, voto2):
	return voto1[1] == voto2[0] or voto1[0] == voto2[1]

def votacao(gatos, caes, votos):
	votos_x
	if len(votos) >= 2:
		for outro in votos[1:]:
			votos_x = votos - outro
			if votos_conflitam(votos[0], outro):
				return len(votos)-1
	return len(votos)
