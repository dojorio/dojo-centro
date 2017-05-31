#!/usr/bin/env python
# -*- coding: utf-8 -*-

def procura_alguem_que_escreveu_com_alguem(alguem, papers, d):    
    for paper in papers:
        if alguem in paper:
            for autor in paper:
                if autor not in d:
                    d[autor] = d[alguem] + 1


def numero_de_erdos(papers):
    d = {'Erdos': 0}

    procura_alguem_que_escreveu_com_alguem('Erdos', papers, d)
    procura_alguem_que_escreveu_com_alguem('Juliana', papers, d)

    return d
    for paper in papers:
        for autor in paper:
            if autor in ('Marcos','Ana','Julia'):
                d[autor] = 2
            elif autor in ('Murta'):
                d[autor] = 3
            elif autor != 'Erdos':
                d[autor] = 1

    return d
    