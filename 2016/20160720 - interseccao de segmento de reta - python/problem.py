#!/usr/bin/env python
# -*- coding: utf-8 -*-

def create_reta(point_a, point_b):
    result = []

    if point_a[0] == point_b[0]:
        step = 1

        if point_b[1] < point_a[1]:
            step = -1

        for i in range(point_a[1], point_b[1] + step, step):
            result.append((0, i))

        return result

    return [point_a, point_b]