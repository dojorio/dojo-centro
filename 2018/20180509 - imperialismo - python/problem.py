#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_domination_years(connections):
    number_of_connections = len(connections)
    
    if number_of_connections == 4 and len(set(connections)) == 1:
        return 1

    if number_of_connections == 3 and len(set(connections)) >= 3:
        return 2

    if number_of_connections == 4:
        return 2

    return 1