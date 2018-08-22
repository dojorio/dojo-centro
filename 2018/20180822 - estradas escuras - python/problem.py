#!/usr/bin/env python
# -*- coding: utf-8 -*-

def estradas_escuras(graph_hash):
	max_n = max(n[2] for n in graph_hash)
	
	if len(graph_hash) >= 3:
		return max_n

	return 0