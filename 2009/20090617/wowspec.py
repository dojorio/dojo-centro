class Char:
    def __init__(self):
        self.mode = "idle"
        self.__grito = None
    
    def get_grito(self):
        return self.__grito
        
    def set_grito(self):
        self.__grito = "Filho de python"
        time.sleep(1000)
        del self.__grito
        
    def del_grito(self):s
        self.__grito = None
    
    grito = property(get_grito, set_grito, del_grito)
    
    def get_mode(self):
        return self.mode
    
    def gets_attacked(self, weapon):
        if weapon == "sword":       
            self.grito = "Filho da python!"
            if self.mode == "idle":
                self.mode = "combat"
            elif self.mode == "combat":
                self.mode = "critical"
    
    def attacks(self, char, weapon):
        char.gets_attacked(weapon)