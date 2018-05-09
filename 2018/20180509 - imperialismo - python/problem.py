#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_domination_years(connections):
    number_of_edges = len(connections)
    unique_edges = len(set(connections))

    if number_of_edges < 3 or unique_edges == 1:
        return 1

    if number_of_edges == 3 and unique_edges == 2:
        return 1

    if number_of_edges < 6 and unique_edges < 5:        
        return 2

    return 3