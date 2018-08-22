#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter

def is_connected(graph_hash, graph_hash_2):
	elements_gh = [n[0] for n in graph_hash] + [n[1] for n in graph_hash]
	elements_gh2 = [n[0] for n in graph_hash_2] + [n[1] for n in graph_hash_2]
	return set(elements) == set(elements_gh2)

def estradas_escuras(graph_hash):
	if len(graph_hash) < 3:
		return 0

	while True:
		max_element = max(n[2] for n in graph_hash)
		for n in graph_hash:
			if n[2] == max_element:
				max_element_t = n
		graph_hash_2 = graph_hash.pop(max_element_t)
	
	max_n = max(n[2] for n in graph_hash)
	if len(graph_hash) == 5:
		return sum(sorted([n[2] for n in graph_hash], reverse=True)[0:2])

	return max_n

	