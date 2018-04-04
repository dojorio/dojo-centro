#!/usr/bin/env python
# -*- coding: utf-8 -*-

def paula_game(expression):
    first = ''
    for i, c in enumerate(expression):
        if c.isdigit():
           first += c 
        if c.isalpha():
            op = c
            second = int(expression[i+1:])
            break
    first = int(first)


    if first == second:
        return first * first
    if op.islower():
        return second + first
    return second - first