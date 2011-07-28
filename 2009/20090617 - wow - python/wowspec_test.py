
import unittest
from wowspec import Char

class WowspecTest(unittest.TestCase):
    def test_char_starts_idle(self):
        frodo = Char()
        self.assertEquals("idle", frodo.get_mode())
    
    def test_char_idle_gets_attacked(self):
        frodo = Char()
        frodo.gets_attacked("sword")
        self.assertEquals("combat", frodo.get_mode())
        
    def test_char_in_combat_gets_attacked(self):
        frodo = Char()
        frodo.mode = "combat"
        frodo.gets_attacked("sword")
        mode = frodo.get_mode()
        self.assertEqual("critical", mode)
        
    def test_char_idle_gets_attacked_with_a_banana(self):
        frodo = Char()
        frodo.gets_attacked("banana")
        self.assertEquals("idle", frodo.get_mode())
        
    def test_char_in_combat_mode_gets_attacked_with_a_banana(self):
        frodo = Char()
        frodo.mode = "combat"
        frodo.gets_attacked("banana")
        self.assertEquals("combat", frodo.get_mode())

    def test_char_attack_char(self):
        frodo = Char()
        alex = Char()
        alex.attacks(frodo, "sword")
        self.assertEquals("combat", frodo.get_mode())

    def test_attacked_char_cries_out(self):
        frodo = Char()
        alex = Char()
        self.assertEquals(None, frodo.grito)
        alex.attacks(frodo, "sword")
        self.assertEquals("Filho da python!", frodo.grito)
        
        
        
        
        
        
        
        
        
        
unittest.main()