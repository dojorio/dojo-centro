#!/usr/bin/env python
# -*- coding: utf-8 -*-

def quiz(mia=False, voa=False,
         pena=False, come_banana=False):
    if mia:
        return "gato"
    elif voa:
        if pena:
            return "pombo"
        return "morcego"
    elif pena:
        return "galinha"

    elif come_banana:
        return "macaco"

    return "cachorro"
