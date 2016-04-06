#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import chain
from functools import partial


def wrote_with(author, coauthor, paper):
	return author in paper and coauthor in paper

def wrote_together(author, coauthor):
	return partial(wrote_with, author, coauthor)

def erdos_number(papers, author):
	if author == 'Erdos':
		return 0

	if 'Erdos' not in chain(*papers):
		return None

	if filter(wrote_together(author, 'Erdos'), papers):
		return 1

	if len(papers) == 2:
		return 2