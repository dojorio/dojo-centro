#!/usr/bin/env python
# -*- coding: utf-8 -*-

def wrote_with(paper, author, coauthor):
	if author in paper and coauthor in paper:
		return True
	else:
		return False

def erdos_number(papers, author):
	if author == 'Erdos':
		return 0

	if any(wrote_with(paper, author, 'Erdos') for paper in papers):
		return 1

	if len(papers) == 2:
		return 2

	return None