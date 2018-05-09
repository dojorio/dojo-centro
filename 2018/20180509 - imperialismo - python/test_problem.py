#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1994

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_two_empires(self):
        # 1 - 2
        connections = [1]
        self.assertEqual(
            get_domination_years(connections), 
            1
        )

    def test_four_empires(self):
        # 1 - 2 - 3 - 4
        connections = [1, 2, 3]
        self.assertEqual(
            get_domination_years(connections), 
            2
        )

    def test_four_different_empires(self):
        # 2 - 1 - 3
        #     |
        #     4
        connections = [1, 1, 1]
        self.assertEqual(
            get_domination_years(connections), 
            1
        )

    def test_five_empires(self):
        # 1 - 2 - 3 - 4 - 5
        connections = [1, 2, 3, 4]
        self.assertEqual(
            get_domination_years(connections), 
            2
        )

    def test_five_different_empires(self):
        #     5
        #     |
        # 2 - 1 - 3
        #     |
        #     4
        connections = [1, 1, 1, 1]
        self.assertEqual(
            get_domination_years(connections), 
            1
        )

    def test_three_different_empires(self):
        # 1 - 2 - 3
        connections = [1, 2]
        self.assertEqual(
            get_domination_years(connections), 
            1
        )


    def test_four_different_empires(self):
        # 1 - 2 - 3
        connections = [1, 2]
        self.assertEqual(
            get_domination_years(connections), 
            1
        )

    def test_five_other_different_empires(self):
        # 2 - 1 - 3 - 5
        #     |
        #     4
        connections = [1, 1, 1, 3]
        self.assertEqual(
            get_domination_years(connections), 
            2
        )

    def test_six_empires(self):
        # 1 - 2 - 3 - 4 - 5 - 6
        connections = [1, 2, 3, 4, 5]
        self.assertEqual(
            get_domination_years(connections), 
            3
        )

if __name__ == "__main__":
    unittest.main()

