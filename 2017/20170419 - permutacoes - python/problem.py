#!/usr/bin/env python
# -*- coding: utf-8 -*-

def permutacoes(entrada):
    if len (entrada) > 1:
        return sorted([entrada, entrada[::-1]])

    return [entrada]