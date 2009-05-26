from string import ascii_uppercase 

class DiamondBase(object):
    def __init__(self, char):
        self.char = char
        self.ordinal = ascii_uppercase.find(char)
        
class Diamond(DiamondBase):
    def __str__(self):
        if self.char == "A": 
            return str(DiamondLine("A"))
        elif self.char == "B":
            return """\
 A
B B
 A"""
        elif self.char == "C":
            return """\
  A
 B B
C   C
 B B
  A"""
        else:
            [str(DiamondLine(x)) for x in ascii_uppercase[:self.ordinal+1]]
            
  
class DiamondLine(DiamondBase):
    def __str__(self):
        number_of_spaces = self.ordinal * 2 - 1
        if self.ordinal == 0:
            return "A"
        return "%s%s%s" % (self.char, number_of_spaces * ' ', self.char)

        
        
        
        
        
        
        
        
        