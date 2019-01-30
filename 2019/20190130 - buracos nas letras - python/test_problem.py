	#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestBuracos(unittest.TestCase):
    def test_A_tem_1_buraco(self):
        self.assertEqual(quantidade_buracos('A'), 1)

    def test_B_tem_2_buracos(self):
    	self.assertEqual(quantidade_buracos('B'), 2)


if __name__ == "__main__":
    unittest.main()

