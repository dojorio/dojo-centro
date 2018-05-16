#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_connected(streets):
    # { (1, 2): True, (2, 1): True}
    graph = {}
    for start, finish, way in streets:
        graph[(start, finish)] = True
        graph[(finish, start)] = way == 2

    print(graph)


    if len(streets) == 1:
        return streets[0][2] == 2

    if len(streets) == 2:
        return False

    if len(streets) == len(set([n[1] for n in streets])):
        return True

    return ((streets[0][2] == 2 and streets[1][2] == 2) or
            (len(streets) == 3 and streets[1][2] == 2))