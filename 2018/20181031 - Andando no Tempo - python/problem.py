#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
from collections import Counter

def viagem(anos):
    ocurrences = [n > 1 for n in Counter(anos).values()]
    highest_year = max(anos)
    lower_years = copy.copy(anos)
    lower_years.remove(highest_year)

    if any(ocurrences):
        return "S"

    if highest_year - sum(lower_years) == 0:
        return "S"
        
    return "N"
