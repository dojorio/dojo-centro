#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_spider_busao_1_edge_chegou(self):
        riocard = 10
        bus_graph = [
            (1, 2, 10)
        ]
        self.assertEqual(
            spider_walk(riocard, bus_graph), 
            "Chegou!"
        )

    def test_spider_busao_1_edge_nao_chegou(self):
        riocard = 10
        bus_graph = [
            (1, 2, 11)
        ]
        self.assertEqual(
            spider_walk(riocard, bus_graph), 
            "Chegou!"
        )


if __name__ == "__main__":
    unittest.main()

