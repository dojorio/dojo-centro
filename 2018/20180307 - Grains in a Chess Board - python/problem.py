#!/usr/bin/env python
# -*- coding: utf-8 -*-

def board_to_kg(cells):
    return board_to_g(cells)//1000

def board_to_g(cells):
    return board_to_grain(cells)//12

def board_to_grain(cells):
    return (2 ** cells) - 1
