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
            1 ______
            2 ___|__

        '''
        transformations = [2, 1]
        self.assertEqual(p_network(transformations), [1])


if __name__ == "__main__":
    unittest.main()