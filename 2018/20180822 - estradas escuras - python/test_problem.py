#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_two_nodes_no_economy(self):
        graph_hash = [
            (0, 1, 3)
        ]
        self.assertEqual(estradas_escuras(graph_hash), 0)

    def test_two_nodes_com_economy(self):
        """
        0 - 1
        |  /
        2
        """
        graph_hash = [
            (0, 1, 2),
            (0, 2, 2),
            (1, 2, 2),
        ]
        self.assertEqual(estradas_escuras(graph_hash), 2)

    def test_two_nodes_com_economy_2(self):
        """
        0 - 1
        |  /
        2
        """
        graph_hash = [
            (0, 1, 2),
            (0, 2, 2),
            (1, 2, 3),
        ]
        self.assertEqual(estradas_escuras(graph_hash), 3)

    def test_two_nodes_com_economy_3(self):
        """
        0 - 1
        |   |
        2 - 3
        """
        graph_hash = [
            (0, 1, 2),
            (0, 2, 2),
            (1, 3, 2),
            (2, 3, 2),
        ]
        self.assertEqual(estradas_escuras(graph_hash), 2)

if __name__ == "__main__":
    unittest.main()

