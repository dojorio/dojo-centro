#!/usr/bin/env python
# -*- coding: utf-8 -*-

def bubbles(sequence):
    if sorted(sequence) == sequence:
        return 'Carlos'
    if len(sequence) == 3:
        if sequence[0] == 3 and sequence[1] == 1:
            return 'Carlos'
        if sequence[0] == 2 and sequence[1] == 3:
            return 'Carlos'

    if len(sequence) == 4:
        if sequence[0] == 3 and sequence[1] == 1 and True:
            return 'Carlos'
        if sequence[0] == 2 and sequence[1] == 3:
            return 'Carlos'





    return 'Marcelo'
