#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_domination_years(connections):
    if len(set(connections)) <= 2:
        return 1

    if len(connections) == 3 and len(set(connections)) >= 3:
        return 2

    if len(connections) == 4:
        return 2