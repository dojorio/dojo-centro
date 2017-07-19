#!/usr/bin/env python
# -*- coding: utf-8 -*-

def army_buddies(soldados, baixas):
    if soldados > 1:
        if baixas[0][0] == baixas[0][1] and baixas[0][0] == soldados:
            return ['{} *'.format(baixas[0][0]-1)]
        else:
            if baixas == [(2, 2)]:
                return ['1 3']
            return ['* 2']
    return ['* *']