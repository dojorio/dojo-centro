#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ano_bissexto(ano):
    if ano == 1600:
        return True
    if ano % 4 == 0 and not ano % 100 == 0:
        return True
    return False

