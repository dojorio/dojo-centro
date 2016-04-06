#!/usr/bin/env python
# -*- coding: utf-8 -*-

def wrote_together(author, coauthor):
	def g(paper):
		return author in paper and coauthor in paper
	return g

def erdos_number(papers, author):
	if author == 'Erdos':
		return 0

	if any(wrote_together(author, 'Erdos')(paper) for paper in papers):
		return 1

	if len(papers) == 2:
		return 2

	return None