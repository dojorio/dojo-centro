import unittest
from tree_recovery import tree_recovery

class TreeRecoveryTest(unittest.TestCase):
    def test_one_node(self):
        self.assertEquals(tree_recovery('A', 'A'), 'A')

    def test_A_root_B_left_node(self):
        self.assertEquals(tree_recovery('AB', 'BA'), 'BA')

    def test_B_root_C_left_node(self):
        self.assertEquals(tree_recovery('BC', 'CB'), 'CB')

unittest.main()