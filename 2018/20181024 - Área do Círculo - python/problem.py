#!/usr/bin/env python
# -*- coding: utf-8 -*-

PI = 3.14159 

def area(raio):
	return 'A=' + str("{:.4f}".format(round((raio**2) * PI, 4)))
	

