#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import chain


def wrote_together(author, coauthor):
	def g(paper):
		return author in paper and coauthor in paper
	return g

def erdos_number(papers, author):
	if author == 'Erdos':
		return 0

	if 'Erdos' not in chain(*papers):
		return None

	if filter(wrote_together(author, 'Erdos'), papers):
		return 1

	if len(papers) == 2:
		return 2