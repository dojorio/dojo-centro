#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from animal_quiz import *


class TestProblem(unittest.TestCase):
    def test_cachorro(self):
        self.assertEqual("cachorro", quiz())

    def test_gato(self):
        self.assertNotEqual("gato", quiz())
        self.assertEqual("mia?", quiz(False))
        self.assertEqual("gato", quiz(True))

if __name__ == "__main__":
    unittest.main()

