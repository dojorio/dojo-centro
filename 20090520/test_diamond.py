import unittest
from diamond import *

class DiamondTests(unittest.TestCase):
    def test_A(self):
        diamond = Diamond("A")
        self.assertEqual(str(diamond), "A")

    def test_B(self):
        diamond = Diamond("B")
        self.assertEqual(str(diamond), """\
 A
B B
 A""")
 
    def test_C(self):
        diamond = Diamond("C")
        self.assertEqual(str(diamond), """\
  A
 B B
C   C
 B B
  A""")    

    def test_D(self):
        diamond = Diamond("D")
        self.assertEqual(str(diamond), """\
   A
  B B
 C   C
D     D
 C   C
  B B
   A""")   


class DiamondLineTests(unittest.TestCase):
    def test_diamond_line_A(self):
        line = DiamondLine("A")
        self.assertEqual(str(line), "A")
        
    def test_diamond_line_B(self):
        line = DiamondLine("B")
        self.assertEqual(str(line), "B B")
        
    def test_diamond_line_C(self):
        line = DiamondLine("C")
        self.assertEqual(str(line), "C   C")
        
    def test_diamond_line_D(self):
        line = DiamondLine("D")
        self.assertEqual(str(line), "D     D")
        
        
unittest.main()
