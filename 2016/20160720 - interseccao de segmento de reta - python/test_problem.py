#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sure
import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def test_1(self):
        expected = [(0,0), (1,0)]
        point_a = (0, 0)
        point_b = (1, 0)
        create_reta(point_a, point_b).should.be.equal(expected)

    def test_2(self):
        expected = [(0,0), (0,1)]
        point_a = (0, 0)
        point_b = (0, 1)
        create_reta(point_a, point_b).should.be.equal(expected)

    def test_3(self):
        expected = [(0,0), (0,1), (0,2)]
        point_a = (0, 0)
        point_b = (0, 2)
        create_reta(point_a, point_b).should.be.equal(expected)

    def test_4(self):
        expected = [(0,0), (0,-1), (0,-2)]
        point_a = (0, 0)
        point_b = (0, -2)
        create_reta(point_a, point_b).should.be.equal(expected)

    def test_5(self):
        expected = [(0,0), (1, 0), (2, 0)]
        point_a = (0, 0)
        point_b = (2, 0)
        create_reta(point_a, point_b).should.be.equal(expected)


if __name__ == "__main__":
    unittest.main()

