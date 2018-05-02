#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://codechen.blogspot.com.br/2015/06/leetcode-skyline-problem.html

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    # [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ]
    # [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]
    def test_one_building(self):
        buildings = [
            [2, 9, 10]
        ]
        skyline_coordinates = [
            [2, 10], [9, 0],
        ]
        self.assertEqual(skyline(buildings), skyline_coordinates)

    def test_one_other_building(self):
        buildings = [
            [3, 6, 10]
        ]
        skyline_coordinates = [
            [3, 10], [6, 0],
        ]
        self.assertEqual(skyline(buildings), skyline_coordinates)

    def test_two_separate_buildings(self):
        buildings = [
            [2, 9, 10], 
            [11, 18, 10],
        ]
        skyline_coordinates = [
            [2, 10], [9, 0],
            [11, 10], [18, 0],
        ]
        self.assertEqual(skyline(buildings), skyline_coordinates)

    def test_two_separate_buildings(self):
        buildings = [
            [2, 9, 10], 
            [11, 18, 10],
        ]
        skyline_coordinates = [
            [2, 10], [9, 0],
            [11, 10], [18, 0],
        ]
        self.assertEqual(skyline(buildings), skyline_coordinates)

    def test_three_separate_buildings(self):
        buildings = [
            [2, 9, 10], 
            [11, 18, 10],
            [20, 27, 10],
        ]
        skyline_coordinates = [
            [2, 10], [9, 0],
            [11, 10], [18, 0],
            [20, 10], [27, 0],
        ]
        self.assertEqual(skyline(buildings), skyline_coordinates)

    def test_four_separate_buildings(self):
        buildings = [
            [2, 9, 10], 
            [11, 18, 10],
            [20, 27, 10],
            [29, 36, 10],
        ]
        skyline_coordinates = [
            [2, 10], [9, 0],
            [11, 10], [18, 0],
            [20, 10], [27, 0],
            [29, 10], [36, 0],
        ]
        self.assertEqual(skyline(buildings), skyline_coordinates)


    def test_two_adjacent_buildings_with_same_height(self):
        buildings = [
            [2, 9, 10], 
            [9, 16, 10],
        ]
        skyline_coordinates = [
            [2, 10], [16, 0],
        ]
        self.assertEqual(skyline(buildings), skyline_coordinates)

    def test_two_adjacent_buildings_with_same_height_2(self):
        buildings = [
            [2, 9, 10], 
            [9, 18, 10],
        ]
        skyline_coordinates = [
            [2, 10], [18, 0],
        ]
        self.assertEqual(skyline(buildings), skyline_coordinates)


if __name__ == "__main__":
    unittest.main()

