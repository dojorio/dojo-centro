#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter

def is_connected(graph_hash, graph_hash_2):
	elements_gh = [n[0] for n in graph_hash] + [n[1] for n in graph_hash]
	elements_gh2 = [n[0] for n in graph_hash_2] + [n[1] for n in graph_hash_2]
	return set(elements_gh) == set(elements_gh2)

def estradas_escuras(graph_hash):
	if len(graph_hash) < 3:
		return 0
	
	graph_hash_2 = graph_hash
	tries = len(graph_hash)
	tried_elements = []
	total_economy = 0

	while tries != 0:
		max_element = max([n[2] for n in graph_hash_2 if n not in tried_elements])
		max_element_tuple = [n for n in graph_hash_2 if n[2] == max_element][0]
		tried_elements.append(max_element_tuple)

		for i,graph_tuple in enumerate(graph_hash_2):
			if graph_tuple == max_element_tuple:
				graph_hash_2.pop(i) # remove o de maior valor
				break

		if is_connected(graph_hash, graph_hash_2):
			total_economy += max_element
		tries -= 1

	return total_economy
	