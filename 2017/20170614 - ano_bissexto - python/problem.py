#!/usr/bin/env python
# -*- coding: utf-8 -*-

# O ano for divisível por 4,
#   mas não divisível por 100,
#   exceto se ele for também divisível por 400.

def ano_bissexto(ano):
    
    if ano % 4 == 0 and ano != 100 and ano != 200 and ano != 300 and ano != 500:
        return True

    return False

