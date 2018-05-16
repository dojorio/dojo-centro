#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_connected(streets):
    if len(streets) == 1:
        return streets[0][2] == 2

    return len(streets) == 3 or streets[0][2] == 2 and streets[1][2] == 2