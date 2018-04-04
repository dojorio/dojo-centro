#!/usr/bin/env python
# -*- coding: utf-8 -*-

def converter(inputy):
    if inputy == '10':
        inputy = 'A'

    if inputy == '11':
        inputy = 'B'

    if inputy == '12':
        inputy = 'C'

    return '0x' + inputy