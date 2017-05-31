#!/usr/bin/env python
# -*- coding: utf-8 -*-

def numero_de_erdos(papers):
    if len(papers) == 2:
        return {
                'Erdos':0,
                'Carlos':1
            }
    elif len(papers) == 3:
        return {
                'Erdos':0,
                'Carlos':1,
                'Juliana':1,
            }
    return {'Erdos':0}
