#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/en/problems/view/1274

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_1(self):
        '''
            1 ______ 1
        '''
        transformations = [1]
        self.assertEqual(p_network(transformations), [])

    def test_2_1(self):
        '''
            1 ______ 2
            2 ___|__ 1
        '''
        transformations = [2, 1]
        self.assertEqual(p_network(transformations), [1])

    def test_2_1_3(self):
        '''
            1 _______ 2
            2 ___|___ 1
            3 _______ 3
        '''
        transformations = [2, 1, 3]
        self.assertEqual(p_network(transformations), [1])

    def test_1_3_2(self):
        '''
            1 _______ 1
            2 _______ 3
            3 ___|___ 2
        '''
        transformations = [1, 3, 2]
        self.assertEqual(p_network(transformations), [2])

    def test_2_3_1(self):
        '''
            1 ________ 3
            2 _____|__ 1
            3 ___|____ 2
        '''
        transformations = [2, 3, 1]
        self.assertEqual(p_network(transformations), [2, 1])

    def test_3_1_2(self):
        '''
            1 ________ 2
            2 __|_____ 3
            3 _____|__ 1
        '''
        transformations = [3, 1, 2]
        self.assertEqual(p_network(transformations), [1, 2])

    def test_3_2_1(self):
        '''
            1 ________ 3
            2 __|___|_ 2
            3 ____|___ 1
        '''
        transformations = [3, 2, 1]
        self.assertEqual(p_network(transformations), [1, 2, 1])



if __name__ == "__main__":
    unittest.main()