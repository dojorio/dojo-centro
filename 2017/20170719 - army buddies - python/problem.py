#!/usr/bin/env python
# -*- coding: utf-8 -*-

def army_buddies(soldados, baixas):
    if soldados > 1:
        primeiro = baixas[0][0] - 1
        segundo = baixas[0][1] + 1
        if primeiro == 0:
            primeiro = '*'
        if segundo > soldados:
            segundo = '*'
        return ['{} {}'.format(primeiro, segundo)]
        
    return ['* *']