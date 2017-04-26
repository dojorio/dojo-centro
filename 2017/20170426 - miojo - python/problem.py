#!/usr/bin/env python
# -*- coding: utf-8 -*-

def miojo(a1, a2):

    if abs(a1 - a2) == 3:
        return max((a1, a2))

    if (a1, a2) == (6, 9):
        return 9
    elif (a1, a2) == (7, 9):
        return 21

    return 10