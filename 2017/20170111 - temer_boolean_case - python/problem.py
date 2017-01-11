#!/usr/bin/env python
# -*- coding: utf-8 -*-

def impeachment(votacao):
	votacao = votacao.replace("Ns", "nn")
	votacao = votacao.replace("Sn", "ss")

	return votacao.lower().count("s") > len(votacao)/2


	
