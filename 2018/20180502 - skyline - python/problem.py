#!/usr/bin/env python
# -*- coding: utf-8 -*-

def skyline(buildings):

    result = []

    if (buildings[0][1] == buildings[1][0]):
        building_count = len(buildings)
        result = [
                [buildings[0][0], buildings[0][2]], 
                [buildings[building_count - 1][1], 0]
            ]
    else:
        for building in buildings:
            result += [
                [building[0], building[2]], 
                [building[1], 0]
            ] 
    return result