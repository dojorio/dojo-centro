#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://www.urionlinejudge.com.br/judge/en/problems/view/1069

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_without_diamond(self):
        self.assertEqual(count_diamond(''), 0)


if __name__ == "__main__":
    unittest.main()

