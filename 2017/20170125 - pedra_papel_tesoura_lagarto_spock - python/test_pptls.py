#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from pptls import quem_ganha


class TestPPTLS(unittest.TestCase):
    def test_tesoura_corta_papel(self):
        self.assertEqual("tesoura", quem_ganha("tesoura", "papel"))

if __name__ == "__main__":
    unittest.main()


