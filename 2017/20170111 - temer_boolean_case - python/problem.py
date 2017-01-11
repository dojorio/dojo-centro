#!/usr/bin/env python
# -*- coding: utf-8 -*-

def impeachment(votacao):
	if "S" == votacao[0]: return True
	return 'n' not in votacao.lower()
	
