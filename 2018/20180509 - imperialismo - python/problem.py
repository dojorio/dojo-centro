#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_domination_years(connections):
    if (len(connections) < 3 or len(set(connections)) == 1):
        return 1

    if len(set(connections)) == 2 and len(connections) == 3:
        return 1

    if len(set(connections)) < 5:        
        return 2

    return 3