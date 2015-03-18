# coding: utf-8
import unittest
from jokenpo import jokenpo

class TestJokenpo(unittest.TestCase):
    def test_draw(self):
        self.assertEqual(jokenpo('spock', 'spock'), 'draw')

    def test_spock_and_lizard(self):
        self.assertEqual(jokenpo('spock', 'lizard'), 'play2')

    def test_lizard_and_spock(self):
        self.assertEqual(jokenpo('lizard', 'spock'), 'play1')

    def test_lizard_and_rock(self):
        self.assertEqual(jokenpo('lizard', 'rock'), 'play2')

    def test_rock_and_lizard(self):
        self.assertEqual(jokenpo('rock', 'lizard'), 'play1')

unittest.main()