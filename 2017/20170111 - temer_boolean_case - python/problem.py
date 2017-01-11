#!/usr/bin/env python
# -*- coding: utf-8 -*-

def impeachment(votacao):
	if len(votacao) == 1:
		return votacao.lower() == "s"
	if votacao.count("s") > len(votacao)/2: return True
	if "S" == votacao[0]: return True
	#return 'n' not in votacao.lower()
	
