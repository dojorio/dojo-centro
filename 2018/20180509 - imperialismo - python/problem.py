#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_domination_years(connections):
    number_of_edges = len(connections)
    unique_edges = len(set(connections[1:]))

    max_years = (number_of_edges + 1) // 2 

    if number_of_edges == (unique_edges + 1):
        return max_years

    return 1 + unique_edges // 2
