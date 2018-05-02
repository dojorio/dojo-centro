#!/usr/bin/env python
# -*- coding: utf-8 -*-

def skyline(buildings):
    if len(buildings) >= 2:
        if (buildings[0][1] == buildings[1][0]):
            return [
                [buildings[0][0], buildings[0][2]], 
                [buildings[1][1], 0]
            ]

    result = []
    for building in buildings:
        result += [
            [building[0], building[2]], 
            [building[1], 0]
        ] 
    return result