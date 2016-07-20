#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sure
import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def test_1(self):
        expected = [(0,0), (1,0)]
        create_reta(0,0,1,0).should.be.equal(expected)

    def test_1(self):
        expected = [(0,0), (0,1)]
        create_reta(0,0,0,1).should.be.equal(expected)

if __name__ == "__main__":
    unittest.main()

