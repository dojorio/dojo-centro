#!/usr/bin/env python
# -*- coding: utf-8 -*-

def wrote_with_erdos(paper, author):
	if author in paper and 'Erdos' in paper:
		return True
	else:
		return False

def erdos_number(papers, author):
	if author == 'Erdos':
		return 0
	if any(wrote_with_erdos(paper, author) for paper in papers):
		return 1

	return None