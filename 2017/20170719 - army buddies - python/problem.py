#!/usr/bin/env python
# -*- coding: utf-8 -*-

def army_buddies(soldados, baixas):
    primeiro = baixas[0][0] - 1 or '*'
    segundo = (baixas[0][1] + 1) % (soldados + 1) or '*'
    return ['{} {}'.format(primeiro, segundo)]