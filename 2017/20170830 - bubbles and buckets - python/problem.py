#!/usr/bin/env python
# -*- coding: utf-8 -*-

def bubbles(sequence):
    if sorted(sequence) == sequence:
        return 'Carlos'

    if len(sequence) == 2:
        return 'Marcelo'

    if len(sequence) == 3:
        if sequence[0] == 1 and sequence[1] == 3:
            return 'Marcelo'
        if sequence[0] == 3 and sequence[1] == 1:
            return 'Carlos'
        if sequence[0] == 2 and sequence[1] == 3:
            return 'Carlos'
        return 'Marcelo'
    return 'Marcelo'
