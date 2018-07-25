#!/usr/bin/env python
# -*- coding: utf-8 -*-

def kuro_infection(kuro_number, wires):
	if (wires[0][0] == wires[1][0]):
		return 1 
	return kuro_number + 1