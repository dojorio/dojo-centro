#!/usr/bin/env python
# -*- coding: utf-8 -*-

def erdos_number(papers, author):
	if author == 'Erdos':
		return 0
	if any(author in paper for paper in papers):
		return 1

	return None