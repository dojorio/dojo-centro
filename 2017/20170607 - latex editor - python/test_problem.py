#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_(self):
        self.assertEqual('A', latex('\pstree{\Tcircle{A}}{}'))


if __name__ == "__main__":
    unittest.main()

