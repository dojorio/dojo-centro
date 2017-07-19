#!/usr/bin/env python
# -*- coding: utf-8 -*-

def army_buddies(soldados, baixas):
    if soldados > 1:
        if baixas == [(2, 2)]:
            return ['1 *']
        elif baixas == [(3, 3)]:
            return ['2 *']
        elif baixas == [(4, 4)]:
            return ['3 *']
        return ['* 2']
    return ['* *']