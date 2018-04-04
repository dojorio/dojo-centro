#!/usr/bin/env python
# -*- coding: utf-8 -*-

def converter(inputy):
    dic = {'10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}

    if int(inputy) > 15:
        return '0x10'

    return '0x' + dic.get(inputy, inputy)
