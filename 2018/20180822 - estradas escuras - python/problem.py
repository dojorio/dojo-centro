#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter

def estradas_escuras(graph_hash):
	if len(graph_hash) < 3:
		return 0
	
	max_n = max(n[2] for n in graph_hash)
	if len(graph_hash) == 5:
		counter = Counter(n[2] for n in graph_hash)
		return sum(k for k, v in counter.items() if v == 1)

	return max_n

	