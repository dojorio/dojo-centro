#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://github.com/jonatasemidio/dojo_problems/blob/master/spider-busao.md

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
            "Não Chegou!"
        )

    def test_spider_busao_1_edge_nao_chegou_2(self):
        riocard = 10
        bus_graph = [
            (1, 2, 12)
        ]
        self.assertEqual(
            spider_walk(riocard, bus_graph), 
            "Não Chegou!"
        )

    def test_spider_busao_1_edge_nao_chegou_3(self):
        riocard = 10
        bus_graph = [
            (1, 2, 13)
        ]
        self.assertEqual(
            spider_walk(riocard, bus_graph), 
            "Não Chegou!"
        )

    def test_spider_busao_1_edge_nao_chegou_4(self):
        riocard = 15
        bus_graph = [
            (1, 2, 13)
        ]
        self.assertEqual(
            spider_walk(riocard, bus_graph), 
            "Chegou!"
        )

if __name__ == "__main__":
    unittest.main()

