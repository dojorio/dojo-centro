#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_domination_years(connections):
    number_of_edges = len(connections)
    unique_edges = len(set(connections))

    max_years = (number_of_edges + 1) // 2 

    if number_of_edges == unique_edges:
        return max_years

    if unique_edges == 1:
        return unique_edges

    if number_of_edges < 3:
        return unique_edges

    if number_of_edges == 3 and unique_edges == 2:
        return unique_edges - 1

    if number_of_edges < 6 and unique_edges < 5:        
        return unique_edges

    if number_of_edges <= 6 and unique_edges <= 3:        
        return 2

    return 3