#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_infection_1_wire(self):
        kuro_number = 1
        wires = [
            (1, 2)
        ]
        self.assertEqual(kuro_infection(kuro_number, wires), 2)

    def test_infection_2_wire(self):
        # 1 - 2 - 3
        kuro_number = 2
        wires = [
            (1, 2),
            (2, 3),
        ]
        self.assertEqual(kuro_infection(kuro_number, wires), 3)


if __name__ == "__main__":
    unittest.main()

