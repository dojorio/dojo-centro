#!/usr/bin/env python
# -*- coding: utf-8 -*-

IMPOSSIBLE_REVENGE = "Impossible revenge!"

def kuro_infection(wires, kuro_number):
	if wires[0][0] == wires[1][0]:
		return 3
	return kuro_number + 1

