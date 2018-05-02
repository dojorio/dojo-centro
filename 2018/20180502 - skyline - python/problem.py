#!/usr/bin/env python
# -*- coding: utf-8 -*-

def skyline(buildings):
	return [
        [buildings[0][0], buildings[0][2]], 
        [buildings[0][1], 0],
    ]