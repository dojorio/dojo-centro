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

    def test_3_elements_ordered_01(self):
        sequence = [1, 2, 3]
        self.assertEqual('Carlos', bubbles(sequence))

    def test_3_elements_unordered_02(self):
        sequence = [2, 1, 3]
        self.assertEqual('Marcelo', bubbles(sequence))

    def test_3_elements_unordered_03(self):
        sequence = [3, 2, 1]
        self.assertEqual('Marcelo', bubbles(sequence))

    def test_3_elements_unordered_04(self):
        sequence = [1, 3, 2]
        self.assertEqual('Marcelo', bubbles(sequence))

    def test_3_elements_unordered_05(self):
        sequence = [3, 1, 2]
        self.assertEqual('Carlos', bubbles(sequence))

    def test_3_elements_unordered_06(self):
        sequence = [2, 3, 1]
        self.assertEqual('Carlos', bubbles(sequence))

    def test_4_elements_unordered_01(self):
        sequence = [1, 2, 4, 3]
        self.assertEqual('Marcelo', bubbles(sequence))

    def test_4_elements_unordered_02(self):
        sequence = [2, 1, 4, 3]
        self.assertEqual('Carlos', bubbles(sequence))



if __name__ == "__main__":
    unittest.main()
