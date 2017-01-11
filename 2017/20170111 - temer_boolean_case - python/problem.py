#!/usr/bin/env python
# -*- coding: utf-8 -*-

def impeachment(votacao):
	if "S" in votacao: return True
	return 'n' not in votacao.lower()
	
