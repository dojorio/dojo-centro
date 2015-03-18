# coding: utf-8
import unittest

class TestJokenpo(unittest.TestCase):
    def testEmpate(self):
        self.assertEqual(jokenpo('spock', 'spock'), 'draw')

unittest.main()