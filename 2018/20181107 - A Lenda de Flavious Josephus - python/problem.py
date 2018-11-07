#!/usr/bin/env python
# -*- coding: utf-8 -*-

def josephus(homens, salto):
    os_homi = list(range(1, homens+1))
    pos = 0
    while len(os_homi) > 1:
        pos += salto - 1
        while pos >= len(os_homi):
            pos -= len(os_homi)
        os_homi.pop(pos)

    return os_homi[0]
