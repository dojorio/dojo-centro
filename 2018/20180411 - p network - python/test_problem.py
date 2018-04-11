#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

    def test_2_1_3(self):
        '''
            1 _______ 1
            2 _______ 3
            3 ___|___ 2
        '''
        transformations = [1, 3, 2]
        self.assertEqual(p_network(transformations), [2])

    def test_2_1_3(self):
        '''
            1 ________ 3
            2 _____|__ 1
            3 ___|____ 2
        '''
        transformations = [1, 3, 2]
        self.assertEqual(p_network(transformations), [2])

if __name__ == "__main__":
    unittest.main()