#!/usr/bin/env python
# -*- coding: utf-8 -*-

def paula_game(expression):
    for c in expression:
        if c.isalpha():
            first, second = map(int, expression.split(c))
            break

    if first == second:
        return first**2
    if c.islower():
        return second + first
    return second - first