#!/usr/bin/env python
# -*- coding: utf-8 -*-

def estradas_escuras(graph_hash):
	if len(graph_hash) < 3:
		return 0
	
	max_n = max(n[2] for n in graph_hash)
	
	return max_n

	