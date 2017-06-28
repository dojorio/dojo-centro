#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ruby_warrior(mapa, personagens):
	if "m" in mapa:
		forca_do_warrior = personagens[0][1]
		forca_do_monstro = personagens[1][1]
		vida_do_warrior = personagens[0][0]
		vida_do_monstro = personagens[1][0]
		if vida_do_monstro > vida_do_warrior:
			return False
		if forca_do_warrior < forca_do_monstro:
			return False
	return True