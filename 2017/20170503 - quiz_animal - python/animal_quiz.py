#!/usr/bin/env python
# -*- coding: utf-8 -*-

def quiz(mia=False, voa=False,
         pena=False, come_banana=False, nada=False, 
         couro=False):

    if mia:
        return "gato"
    elif voa:
        if pena:
            return "pombo"
        return "morcego"
    elif pena:
        if nada:
            return "pato"
        return "galinha"

    elif come_banana:
        return "macaco"
    elif couro:
        return "hipopotamo"

    
    return "cachorro"

