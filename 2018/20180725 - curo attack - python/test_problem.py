#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):

    def test_infection_2_wire(self):
        wires = [
            (1, 2),
            (2, 3),
        ]
        self.assertEqual(
            kuro_infection(wires, kuro_number=2), 3)

    def test_infection_3_wire(self):
        wires = [
            (1, 2),
            (2, 3),
            (3, 4),
        ]
        self.assertEqual(
            kuro_infection(wires, kuro_number=3), 4)   

    def test_infection_4_wire(self):
        wires = [
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
        ]
        self.assertEqual(
            kuro_infection(wires, kuro_number=3), 4)

    def test_infection_5_wire(self):
        wires = [
            (1, 2),
            (1, 3),
        ]
        self.assertEqual(
            kuro_infection(wires, kuro_number=2), 4)    

    # def test_infection_6_wire(self):
    #     # Kuro-number (2 ≤ K < N ≤ 1000)
    #     # 1 - 2
    #     # |
    #     # 3
    #     kuro_number = 2
    #     wires = [
    #         (1, 2),
    #         (1, 3),
    #     ]
    #     self.assertEqual(kuro_infection(kuro_number, wires), 1)    


if __name__ == "__main__":
    unittest.main()

