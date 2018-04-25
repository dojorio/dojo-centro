#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://github.com/jonatasemidio/dojo_problems/blob/master/spider-busao.md

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_spider_busao_1_edge_chegou_1(self):
        riocard = 10
        bus_graph = [
            (1, 2, 10)
        ]
        self.assertEqual(
            spider_walk(riocard, bus_graph), 
            "Chegou!"
        )

    def test_spider_busao_1_edge_nao_chegou_1(self):
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

    def test_spider_busao_1_edge_chegou_2(self):
        riocard = 15
        bus_graph = [
            (1, 2, 13)
        ]
        self.assertEqual(
            spider_walk(riocard, bus_graph), 
            "Chegou!"
        )

    def test_spider_busao_1_edge_chegou_3(self):
        riocard = 16
        bus_graph = [
            (1, 2, 13)
        ]
        self.assertEqual(
            spider_walk(riocard, bus_graph), 
            "Chegou!"
        )

    def test_spider_busao_1_edge_chegou_4(self):
        riocard = 17
        bus_graph = [
            (1, 2, 13)
        ]
        self.assertEqual(
            spider_walk(riocard, bus_graph), 
            "Chegou!"
        )

    def test_spider_busao_2_edges_nao_chegou_1(self):
        riocard = 17
        bus_graph = [
            (1, 2, 13),
            (2, 3, 18),
        ]

        self.assertEqual(
            spider_walk(riocard, bus_graph), 
            "Não Chegou!"
        )

    def test_spider_busao_2_edges_chegou_1(self):
        riocard = 17
        bus_graph = [
            (1, 2, 13),
            (2, 3, 17),
        ]

        self.assertEqual(
            spider_walk(riocard, bus_graph), 
            "Chegou!"
        )

    def test_spider_busao_2_edges_nao_chegou_2(self):
        riocard = 7
        bus_graph = [
            (1, 2, 8),
            (2, 3, 7),
        ]

        self.assertEqual(
            spider_walk(riocard, bus_graph), 
            "Não Chegou!"
        )

if __name__ == "__main__":
    unittest.main()

