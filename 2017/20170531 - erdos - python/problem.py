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

    l = list(d.items())
    for autor, numero in l:
        if numero == 1:
            procura_alguem_que_escreveu_com_alguem(autor, papers, d)

    procura_alguem_que_escreveu_com_alguem('Julia', papers, d)

    return d
    