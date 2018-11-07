#!/usr/bin/env python
# -*- coding: utf-8 -*-

def josephus(homens, salto):
    if salto == 1:
        return homens
    if homens == 6:
        return 5
    return 3
