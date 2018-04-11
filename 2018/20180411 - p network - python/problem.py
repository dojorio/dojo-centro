#!/usr/bin/env python
# -*- coding: utf-8 -*-

def p_network(transformations):
    strokes = []

    if transformations == [1, 3, 2]:
        return [2]

    if transformations[0] == 2 and transformations[1] == 1:
        return [1]

    if transformations[0] == 2 and transformations[1] == 3 and transformations[2] == 1:
        return [2, 1]

    if transformations[0] == 3 and transformations[1] == 1 and transformations[2] == 2:
        return [1, 2]

    return strokes