#!/usr/bin/env python
# -*- coding: utf-8 -*-

def miojo(a1, a2):

    if 3 in (a1, a2):
        return 3

    elif abs(a1 - a2) == 3:
        return max((a1, a2))

    t1, t2, t = a1, a2, max((a1, a2))
    while abs(t1 - t2) != 3:
        while 0 not in (t1, t2):
            t1 -= 1
            t2 -= 1
            t += 1
        if t1 == 0:
            t1 = a1
        if t2 == 0:
            t2 = a2
    return t
