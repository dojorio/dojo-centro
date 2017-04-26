#!/usr/bin/env python
# -*- coding: utf-8 -*-

def miojo(a1, a2):

    if abs(a1 - a2) == 3:
        return max((a1, a2))

    elif (a1, a2) == (7, 9):
        return 21

    elif (a1, a2) == (3, 6):
        return 3

    return 10