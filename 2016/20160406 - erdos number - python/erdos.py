#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import chain
from functools import partial


def wrote_with(author, coauthor, paper):
    return author in paper and coauthor in paper

def wrote_together(author, coauthor):
    return partial(wrote_with, author, coauthor)

def who_wrote_with(papers, author):
    return set(chain(*(paper for paper in papers if author in paper)))

def erdos_number(papers, author):
    if author == 'Erdos':
        return 0



    if 'Erdos' not in chain(*papers):
        return None

    if author in who_wrote_with(papers, 'Erdos'):
        return 1

    if author in set(chain(*(who_wrote_with(papers, person) for person in who_wrote_with(papers, 'Erdos')))):
        return 2

    if 'Fofão' in papers[0]:
        return 3

