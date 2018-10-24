#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def circulo_1(self):
        self.assertEqual(area(1), 2)


if __name__ == "__main__":
    unittest.main()

