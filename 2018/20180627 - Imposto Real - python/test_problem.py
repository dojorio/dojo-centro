#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/2666

from problem import *

class TestOneTrip:
    def test_1(self):
        "capacity 1, debits 0 1, road 1"
        assert traveled_distance(1, [0, 1], [(1, 2, 1)]) == 2

    def test_2(self):
        "capacity 1, debits 0 1, road 2"
        assert traveled_distance(1, [0, 1], [(1, 2, 2)]) == 4

    def test_5(self):
        "capacity 2, debits 0 2, road 1"
        assert traveled_distance(2, [0, 2], [(1, 2, 1)]) == 2

class TestManyTrips:
    def test_3(self):
        "capacity 1, debits 0 2, road 1"
        assert traveled_distance(1, [0, 2], [(1, 2, 1)]) == 4

    def test_4(self):
        "capacity 1, debits 0 3, road 1"
        assert traveled_distance(1, [0, 3], [(1, 2, 1)]) == 6

class TestUnderCapacityTrips:
    def test_6(self):
        "capacity 2, debits 0 5, road 1"
        assert traveled_distance(2, [0, 5], [(1, 2, 1)]) == 6

    def test_n(self):
        "capacity 1, debits 0 0, road 2"
        roads = [(1, 2, 2)]
        assert traveled_distance(1, [0, 0], roads) == 0

class TestCitiesOriginIn1:
    def test_7(self):
        "Two cities with 1 as origin"
        assert traveled_distance(1, [0, 1, 1], [(1, 2, 1), (1, 3, 1)]) == 4

    def test_8(self):
        "Two cities with 1 as origin, city 3 far"
        assert traveled_distance(1, [0, 1, 1], [(1, 2, 1), (1, 3, 2)]) == 6

    def test_9(self):
        "Two cities with 1 as origin, city 2 debit is greater"
        assert traveled_distance(1, [0, 2, 1], [(1, 2, 1), (1, 3, 1)]) == 6

    def test_10(self):
        "Two cities with 1 as origin, city 2 debit is greater, unorder roads"
        assert traveled_distance(1, [0, 2, 1], [(1, 3, 2), (1, 2, 1)]) == 8

    def test_11(self):
        "Two cities with 1 as origin, city 2 debit is greater, unorder roads and cities"
        assert traveled_distance(1, [0, 2, 1], [(3, 1, 2), (2, 1, 1)]) == 8

class TestAlignedCities:
    def test_12(self):
        "City 3 has more debit"
        assert traveled_distance(1, [0, 1, 2], [(1, 2, 1), (2, 3, 1)]) == 10

