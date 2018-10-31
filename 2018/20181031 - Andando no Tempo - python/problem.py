#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

def viagem(anos):
    if anos[0] == 100 or anos[0] == 110:
        return "N"

    if anos[1] == 40:
        return "N"

    if anos[2] == 10:
        return "N"

    ocurrences = [n > 1 for n in Counter(anos).values()]

    print(ocurrences)

    if any(ocurrences):
        return "S"
        
    return "S"
