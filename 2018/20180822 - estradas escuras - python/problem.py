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
	graph_hash_tries = graph_hash
	tries = len(graph_hash)
	tried_elements = []
	total_economy = 0

	while tries != 0:
		graph_hash_2 = graph_hash
		for n in graph_hash_2:
			if n not in tried_elements:
				tried_elements.append(n)
			max_element = n[2]

		for i in range(len(graph_hash_2) - 1):
			if graph_hash_2[i][2] == max_element:
				graph_hash_2.pop(max_element)

		if is_connected(graph_hash, graph_hash_2):
			total_economy += max_element
		else:
			graph_hash_2 = graph_hash
		tries -= 1

	return total_economy
	