#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *

        #   VIDA  FORÇA
class TestProb_monstro(unittest.TestCase):
    def test_1_sem_monstro(self):
        #   VIDA  FORÇA/s
        w = [2, 1]
        self.assertTrue(ruby_warrior('W*', [w]))

    def test_2_um_monstro(self):
        #   VIDA  FORÇA
        w = [2,   1   ]
        m = [1,   1   ]
        self.assertTrue(ruby_warrior('Wm*', [w, m]))

    def test_3_um_monstro_forte(self):
        #   VIDA  FORÇA
        w = [2,   1   ]
        m = [2,   2   ]
        self.assertFalse(ruby_warrior('Wm*', [w, m]))

    



if __name__ == "__main__":
    unittest.main()

