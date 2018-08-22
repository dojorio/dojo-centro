#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter

def estradas_escuras(graph_hash):
	if len(graph_hash) < 3:
		return 0
	
	max_n = max(n[2] for n in graph_hash)
	if len(graph_hash) == 5:
		counter = Counter(n[2] for n in graph_hash)
		print(sorted(n[2] for n in graph_hash, reverse=True)[0:2])
		return sum(sorted(n[2] for n in graph_hash, reverse=True)[0:2])

	return max_n

	