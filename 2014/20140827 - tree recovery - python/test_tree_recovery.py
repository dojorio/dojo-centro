import unittest
from tree_recovery import tree_recovery

class TreeRecoveryTest(unittest.TestCase):
    def test_one_node(self):
        self.assertEquals(tree_recovery('A', 'A'), 'A')

    def test_A_root_B_left_node(self):
        self.assertEquals(tree_recovery('AB', 'BA'), 'BA')

    def test_B_root_C_left_node(self):
        self.assertEquals(tree_recovery('BC', 'CB'), 'CB')

    def test_B_root_C_right_node(self):
        self.assertEquals(tree_recovery('BC', 'BC'), 'CB')

    def test_A_root_B_left_C_right(self):
        self.assertEquals(tree_recovery('ABC', 'BAC'), 'BCA')

    def test_A_root_B_left_C_left(self):
        self.assertEquals(tree_recovery('ABC', 'CBA'), 'CBA')

    def test_A_root_B_left_C_right_child(self):
        self.assertEquals(tree_recovery('ABC', 'BCA'), 'CBA')

    def test_(self):
        """
             A
           B   C
         D
        """
        self.assertEquals(tree_recovery('ABDC', 'DBAC'), 'DBCA')

    def test__(self):
        self.assertEquals(tree_recovery('DBACEGF', 'ABCDEFG'), 'ACBFGED')

unittest.main()