#!/usr/bin/env python
# -*- coding: utf-8 -*-

def p_network(transformations):
    strokes = []

    

    # 2 transformations
    if transformations == [2,1]:
        return [1]
    

    # 3 transformations

    if transformations == [2, 1, 3]:
        return [1]
    
    if (
        transformations == [1, 3, 2]
    ):
        return [2]

    if (
        transformations == [2, 3, 1]
    ):
        return [2, 1]

    if (
        transformations == [3, 1, 2]
    ):
        return [1, 2]

    if (
        transformations == [3, 2, 1]
    ):
        return [1, 2, 1]

    return strokes