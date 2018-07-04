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
