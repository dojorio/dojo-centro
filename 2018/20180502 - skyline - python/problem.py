#!/usr/bin/env python
# -*- coding: utf-8 -*-

def skyline(buildings):
    result = []

    building_count = len(buildings)
    if building_count > 1:
        if (buildings[0][1] == buildings[1][0] and buildings[1][1] == buildings[2][0]):
            return [
                    [buildings[0][0], buildings[0][2]], 
                    [buildings[building_count - 1][1], 0]
                ]

    for building in buildings:
        result += [
            [building[0], building[2]], 
            [building[1], 0]
        ] 
    return result