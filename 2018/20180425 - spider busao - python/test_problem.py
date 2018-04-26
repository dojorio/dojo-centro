#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://github.com/jonatasemidio/dojo_problems/blob/master/spider-busao.md

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_spider_busao_1_edge_chegou_1(self):
        minascard = 10
        bus_graph = [
            (1, 2, 10)
        ]
        self.assertEqual(
            spider_walk(minascard, bus_graph), 
            "Chegou!"
        )

    def test_spider_busao_1_edge_nao_chegou_1(self):
        minascard = 10
        bus_graph = [
            (1, 2, 11)
        ]
        self.assertEqual(
            spider_walk(minascard, bus_graph), 
            "Não Chegou!"
        )

    def test_spider_busao_1_edge_nao_chegou_2(self):
        minascard = 10
        bus_graph = [
            (1, 2, 12)
        ]
        self.assertEqual(
            spider_walk(minascard, bus_graph), 
            "Não Chegou!"
        )

    def test_spider_busao_1_edge_nao_chegou_3(self):
        minascard = 10
        bus_graph = [
            (1, 2, 13)
        ]
        self.assertEqual(
            spider_walk(minascard, bus_graph), 
            "Não Chegou!"
        )

    def test_spider_busao_1_edge_chegou_2(self):
        minascard = 15
        bus_graph = [
            (1, 2, 13)
        ]
        self.assertEqual(
            spider_walk(minascard, bus_graph), 
            "Chegou!"
        )

    def test_spider_busao_1_edge_chegou_3(self):
        minascard = 16
        bus_graph = [
            (1, 2, 13)
        ]
        self.assertEqual(
            spider_walk(minascard, bus_graph), 
            "Chegou!"
        )

    def test_spider_busao_1_edge_chegou_4(self):
        minascard = 17
        bus_graph = [
            (1, 2, 13)
        ]
        self.assertEqual(
            spider_walk(minascard, bus_graph), 
            "Chegou!"
        )

    def test_spider_busao_2_edges_nao_chegou_1(self):
        minascard = 17
        bus_graph = [
            (1, 2, 13),
            (2, 3, 18),
        ]

        self.assertEqual(
            spider_walk(minascard, bus_graph), 
            "Não Chegou!"
        )

    def test_spider_busao_2_edges_chegou_1(self):
        minascard = 17
        bus_graph = [
            (1, 2, 13),
            (2, 3, 17),
        ]

        self.assertEqual(
            spider_walk(minascard, bus_graph), 
            "Chegou!"
        )

    def test_spider_busao_2_edges_nao_chegou_2(self):
        minascard = 7
        bus_graph = [
            (1, 2, 8),
            (2, 3, 7),
        ]

        self.assertEqual(
            spider_walk(minascard, bus_graph), 
            "Não Chegou!"
        )

    def test_spider_busao_3_edges_nao_chegou_1(self):
        minascard = 7
        bus_graph = [
            (1, 2, 7),
            (2, 3, 8),
            (3, 4, 7),
        ]

        self.assertEqual(
            spider_walk(minascard, bus_graph), 
            "Não Chegou!"
        )

    def test_spider_busao_3_edges_chegou_1(self):
        minascard = 5
        bus_graph = [
            (1, 2, 5),
            (2, 3, 5),
            (1, 3, 6),
        ]

        self.assertEqual(
            spider_walk(minascard, bus_graph), 
            "Chegou!"
        )

    def test_spider_busao_de_volta_ao_lar(self):
        minascard = 25
        bus_graph = [
            (1, 2, 20),
            (1, 3, 10),
            (2, 4, 10),
            (2, 5, 25),
            (4, 6, 25),
            (5, 6, 27),
            (3, 6, 30),
        ]

        self.assertEqual(
            spider_walk(minascard, bus_graph), 
            "Chegou!"
        )

if __name__ == "__main__":
    unittest.main()

