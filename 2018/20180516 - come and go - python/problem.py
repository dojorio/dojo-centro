#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_connected(streets):
    graph = {}

    for start, finish, way in streets:
        graph[(start, finish)] = True
        graph[(finish, start)] = way == 2

    return list(graph.values()).count(True) >= 3

    if len(streets) == 1:
        return streets[0][2] == 2

    if len(streets) == 2:
        return False

    if len(streets) == len(set([n[1] for n in streets])):
        return True

    return ((streets[0][2] == 2 and streets[1][2] == 2) or
            (len(streets) == 3 and streets[1][2] == 2))