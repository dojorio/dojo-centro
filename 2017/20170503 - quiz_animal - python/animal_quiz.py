#!/usr/bin/env python
# -*- coding: utf-8 -*-

#mia, voa, pena, come_banana, nada, couro
animal= {
(  1,   0,    0,           0,    0,     0): 'gato',
(  0,   1,    1,           0,    0,     0): 'pombo',
(  0,   1,    0,           0,    0,     0): 'morcego', 
(  0,   0,    1,           0,    1,     0): 'pato',
(  0,   0,    1,           0,    0,     0): 'galinha',
}
def quiz(mia=False, voa=False,
         pena=False, come_banana=False, nada=False, 
         couro=False):

    return animal[(mia, voa, pena, come_banana, nada, couro)]

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

