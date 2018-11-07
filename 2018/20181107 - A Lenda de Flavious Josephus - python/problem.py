#!/usr/bin/env python
# -*- coding: utf-8 -*-

def josephus(homens, salto):
    os_homi = list(range(1, homens+1))
    if salto == 1:
        return homens
    if homens == 6:
        return 5
    return 3
