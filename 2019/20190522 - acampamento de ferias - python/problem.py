#!/usr/bin/env python
# -*- coding: utf-8 -*-

def gira(criancas):
	pos = 0
    crianca, numero = criancas.items()
	while len(criancas) > 1:
        list(criancas.keys())[pos]	   

	if list(criancas.values())[0] % 2 == 0:
		return list(criancas)[1]
	return list(criancas)[0]