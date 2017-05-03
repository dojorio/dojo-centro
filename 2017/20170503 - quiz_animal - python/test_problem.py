#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from animal_quiz import *


class TestProblem(unittest.TestCase):
    def test_cachorro(self):
        self.assertEqual("cachorro", quiz())

    def test_gato(self):
        self.assertEqual("gato", quiz())
    

if __name__ == "__main__":
    unittest.main()

