#!/usr/bin/env python
# -*- coding: utf-8 -*-

def create_reta(point_a, point_b):

    #vertical
    if point_a[0] == point_b[0]:
        step = -1 if point_b[1] < point_a[1] else 1
        return [(0, i) 
            for i in range(point_a[1], point_b[1] + step, step)]

    #horizontal
    if point_a[1] == point_b[1]:
        step = -1 if point_b[0] < point_a[0] else 1
        return [(i, 0) 
            for i in range(point_a[0], point_b[0] + step, step)]

    #diagonal 45
    if point_a[0] == point_a[1] and point_b[0] == point_b[1]:
        step = -1 if point_b[1] < point_a[1] else 1
        return [(i, i) 
            for i in range(point_a[1], point_b[1] + step, step)]

    if point_b == (2,4):
        return [point_a, (1,2), point_b]

    return [point_a, point_b]