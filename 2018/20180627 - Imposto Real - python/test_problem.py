#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/2666

from problem import *

def test_1():
    "capacity 1, debits 0 1, road 1"
    assert traveled_distance(1, [0, 1], [(1, 2, 1)]) == 2

def test_2():
    "capacity 1, debits 0 1, road 2"
    assert traveled_distance(1, [0, 1], [(1, 2, 2)]) == 4

def test_3():
    "capacity 1, debits 0 2, road 1"
    assert traveled_distance(1, [0, 2], [(1, 2, 1)]) == 4

def test_4():
    "capacity 1, debits 0 3, road 1"
    assert traveled_distance(1, [0, 3], [(1, 2, 1)]) == 6

def test_5():
    "capacity 2, debits 0 2, road 1"
    assert traveled_distance(2, [0, 2], [(1, 2, 1)]) == 2

def test_n():
    "capacity 1, debits 0 0, road 2"
    roads = [(1, 2, 2)]
    assert traveled_distance(1, [0, 0], roads) == 0