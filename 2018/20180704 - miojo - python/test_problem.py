#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.dojopuzzles.com/problemas/exibe/problema-do-miojo/
from problem import *


class TestProblem:

    def test_ampulheta_3_e_ampulheta_3(self):
        assert miojo(3, 3) == 3

    def test_ampulheta_2_e_ampulheta_5(self):
        assert miojo(2, 5) == 5

    def test_ampulheta_2_e_ampulheta_7(self):
        assert miojo(2, 7) == 7

    def test_ampulheta_7_e_ampulheta_2(self):
        assert miojo(7, 2) == 7

    def test_ampulheta_5_e_ampulheta_7(self):
        assert miojo(5, 7) == 10

    def test_ampulheta_7_e_ampulheta_5(self):
        assert miojo(7, 5) == 10

    def test_ampulheta_8_e_ampulheta_5(self):
        assert miojo(8, 5) == 8

    def test_ampulheta_5_e_ampulheta_8(self):
        assert miojo(5, 8) == 8

    def test_ampulheta_3_e_ampulheta_8(self):
        assert miojo(3, 8) == 3

    def test_ampulheta_5_e_ampulheta_13(self):
        assert miojo(5, 13) == 13

    def test_ampulheta_1_e_ampulheta_2(self):
        assert miojo(1, 2) == 3

    def test_ampulheta_4_e_ampulheta_1(self):
        assert miojo(4, 1) == 3

    def test_ampulheta_2_e_ampulheta_2(self):
        assert miojo(2, 2) == IMPOSSIVEL

    def test_ampulheta_4_e_ampulheta_9(self):
        assert miojo(4, 9) == 12

    def test_ampulheta_4_e_ampulheta_13(self):
        assert miojo(4, 13) == 16