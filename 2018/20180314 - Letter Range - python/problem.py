#!/usr/bin/env python
# -*- coding: utf-8 -*-

def letter_range(str):
    str = str.replace(' ', '')

    if str == '':
        return []

    str = sorted(set(str))

    if len(str) == 2:       
        if (ord(str[1]) - ord(str[0]) == 1):
            return [str[0]+":"+str[1]]

        else:
            return [str[0]+":"+str[0], str[1]+":"+str[1]]

    if len(str) == 3:
        return [str[0]+":"+str[2]]

    return [str[0]+":"+str[0]]