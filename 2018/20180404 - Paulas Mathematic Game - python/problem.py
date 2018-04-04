#!/usr/bin/env python
# -*- coding: utf-8 -*-

def paula_game(expression):
    first = int(expression[0])
    op = expression[1]
    second = int(expression[2])

    if len(expression) > 3:
        expression[2:] - second
    if first == second:
        return first * first
    if op.islower():
        return second + first
    return second - first