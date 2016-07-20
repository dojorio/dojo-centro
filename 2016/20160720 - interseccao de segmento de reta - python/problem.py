#!/usr/bin/env python
# -*- coding: utf-8 -*-

def create_reta(point_a, point_b):
    if (point_b == (0,2)):
        return [point_a, (0,1), point_b]
    return [point_a, point_b]