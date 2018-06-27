#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/2666

from problem import *

def test_1():
    "capacity 1, debits 0 1, road 1"
    assert traveled_distance(1, [0, 1], [(1, 2, 1)]) == 1

def test_2():
    "capacity 1, debits 0 1, road 2"
    assert traveled_distance(1, [0, 1], [(1, 2, 2)]) == 2

