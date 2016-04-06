#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from erdos import *

class TestErdos(unittest.TestCase):
    def test_erdos(self):
    	papers = []
        self.assertEqual(erdos_number(papers, 'Erdos'), 0)

    def test_with_erdos(self):
    	papers = [['Erdos', 'John']]
        self.assertEqual(erdos_number(papers, 'John'), 1)

    def test_without_erdos(self):
    	papers = [['Mary', 'John']]
        self.assertEqual(erdos_number(papers, 'John'), )

if __name__ == "__main__":
    unittest.main()
