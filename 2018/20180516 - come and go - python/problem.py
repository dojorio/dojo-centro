#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_connected(streets):
    graph = {}
    destination_intersection = max([street[0] for street in streets] + 
        [street[1] for street in streets])
    print(destination_intersection)

    def walk(graph, current_node):
        if current_node[1] == destination_intersection:
            return graph

        walk(graph, current_node)


    for start, finish, way in streets:
        graph[(start, finish)] = True
        graph[(finish, start)] = way == 2

    print(graph)
    print(all(graph.values()))

    return all(graph.values())

    if len(streets) == 1:
        return streets[0][2] == 2

    if len(streets) == 2:
        return False

    if len(streets) == len(set([n[1] for n in streets])):
        return True

    return ((streets[0][2] == 2 and streets[1][2] == 2) or
            (len(streets) == 3 and streets[1][2] == 2))