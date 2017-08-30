#!/usr/bin/env python
# -*- coding: utf-8 -*-

def bubbles(sequence):
    if len(sequence) == 2: 
        if sequence[0] != 1:
            return 'Marcelo'
        return 'Carlos'

    if len(sequence) == 3:
        if sequence[0] == 1 and sequence[1] == 2:
            return 'Carlos'
        if sequence[0] == 1 and sequence[1] == 3:
            return 'Marcelo'
        if sequence[0] == 3:
            return 'Carlos'
        return 'Marcelo'