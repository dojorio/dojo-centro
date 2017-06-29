#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ruby_warrior(mapa, personagens):
	if "m" in mapa:
		forca_do_warrior = personagens[0][1]
		forca_do_monstro = personagens[1][1]
		vida_do_warrior = personagens[0][0]
		vida_do_monstro = personagens[1][0]
		total_warrior = forca_do_warrior + vida_do_warrior
		total_monstro = forca_do_monstro + vida_do_monstro
		natg = vida_do_monstro/forca_do_warrior
		natm = vida_do_warrior/forca_do_monstro
		return natm > natg

	return True