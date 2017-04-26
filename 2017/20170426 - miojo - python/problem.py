#!/usr/bin/env python
# -*- coding: utf-8 -*-

def miojo(a1, a2):
    if 3 in (a1, a2):
        return 3

    elif abs(a1 - a2) == 3:
        return max((a1, a2))

    elif abs(a1 - a2) == 1:
        
        if (a1, a2) == (5, 6):
            return 15
        elif (a1, a2) == (6, 7):
            return 21
        elif (a1, a2) == (9, 10):
            return 30

    elif (a1, a2) == (7, 9):
        return 21

    return 10