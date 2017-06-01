#!/usr/bin/env python
# -*- coding: utf-8 -*-

def panqueca(alguem, papers, d):    
    for paper in papers:
        if alguem in paper:
            for autor in paper:
                if autor not in d:
                    d[autor] = d[alguem] + 1

def pacoca(nivel, papers, d):
    l = list(d.items())
    for autor, numero in l:
        if numero == nivel:
            panqueca(autor, papers, d)

def numero_de_erdos(papers):
    d = {'Erdos': 0}

    panqueca('Erdos', papers, d)
    for x in range(1,10):
        pacoca(x, papers, d)


    return d
    