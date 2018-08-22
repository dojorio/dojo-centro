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

    def test_two_nodes_com_economy_02(self):
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

    def test_two_nodes_com_economy_03(self):
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

    def test_two_nodes_com_economy_04(self):
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

    def test_two_nodes_com_economy_05(self):
        """
        0 - 1
        | \ |
        2 - 3 
        """
        graph_hash = [
            (0, 1, 2),
            (0, 2, 3),
            (1, 3, 4),
            (2, 3, 2),
            (0, 3, 2)
        ]
        self.assertEqual(estradas_escuras(graph_hash), 7)

    def test_two_nodes_com_economy_06(self):
        """
        0 - 1
        | \ |
        2 - 3 
        """
        graph_hash = [
            (0, 1, 2),
            (0, 2, 3),
            (1, 3, 5),
            (2, 3, 2),
            (0, 3, 2)
        ]
        self.assertEqual(estradas_escuras(graph_hash), 8)

    def test_two_nodes_com_economy_07(self):
        """
        0 - 1
        | \ |
        2 - 3 
        """
        graph_hash = [
            (0, 1, 2),
            (0, 2, 3),
            (1, 3, 3),
            (2, 3, 2),
            (0, 3, 2)
        ]
        self.assertEqual(estradas_escuras(graph_hash), 6)

    def test_two_nodes_com_economy_08(self):
        """
        0 - 1
        | \ |
        2 - 3 
        
        0 - 1
          \ 
        2 - 3 
        """
        graph_hash = [
            (0, 1, 5),
            (0, 2, 2),
            (1, 3, 10),
            (2, 3, 2),
            (0, 3, 2)
        ]
        self.assertEqual(estradas_escuras(graph_hash), 12)

if __name__ == "__main__":
    unittest.main()

