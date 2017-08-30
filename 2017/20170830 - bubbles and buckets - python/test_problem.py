#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/en/problems/view/1088

import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def test_2_elements_ordered(self):
        sequence = [1, 2]
        self.assertEqual('Carlos', bubbles(sequence))

    def test_2_elements_unordered(self):
        sequence = [2, 1]
        self.assertEqual('Marcelo', bubbles(sequence))


if __name__ == "__main__":
    unittest.main()
