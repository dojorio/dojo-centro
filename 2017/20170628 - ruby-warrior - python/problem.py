#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ruby_warrior(warrior, mapa):
	if (len(mapa) > 1) and mapa[0][1] < mapa [1][1]:
		return False
	return True