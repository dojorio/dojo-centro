#!/usr/bin/env python
# -*- coding: utf-8 -*-

def numero_de_erdos(papers):
    d = {}
    for paper in papers:
        for autor in paper:
            if autor == 'Erdos':
                d[autor] = 0
            else: 
                d[autor] = 1

    return d
    