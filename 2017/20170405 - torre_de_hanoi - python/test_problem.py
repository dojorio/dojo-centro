#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_rodelas(self):
        self.assertEqual(3,rodelas(3))
    def test_rodelas_com_2(self):
        self.assertEqual(3,rodelas(2))


if __name__ == "__main__":
    unittest.main()

