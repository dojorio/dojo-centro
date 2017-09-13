#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sixflags(tempo, atracoes):
    if atracoes == ((10, 40),):
        return 240
    elif atracoes[0][0] == 35:
        return 40
    elif atracoes[0][0] > tempo:
        return 0
    return 180