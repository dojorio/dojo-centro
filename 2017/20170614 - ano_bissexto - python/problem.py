#!/usr/bin/env python
# -*- coding: utf-8 -*-

# O ano for divisível por 4,
#   mas não divisível por 100,
#   exceto se ele for também divisível por 400.

def ano_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0