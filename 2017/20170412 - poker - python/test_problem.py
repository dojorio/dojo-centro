#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


# Ouro (D), Copa (H), Espadas (S), Paus (C)

class TestProblem(unittest.TestCase):
    def test_(self):
        self.assertEqual(2, poker('5C 5P 6E 7E KO', '2P 3E 8E 8O TO'))


if __name__ == "__main__":
    unittest.main()

