class WordWrapper:
    def __init__(self, cols):
        self.cols = cols
        
    def wrap(self, text):
        if len(text) <= self.cols:
            return text
        else:
            cols = self.cols
            onde_esta_o_espaco = text[:cols].rfind(" ")
            if (onde_esta_o_espaco == -1):
                return text[:cols] + '\n' + self.wrap(text[cols:])
            else:
                return text[:onde_esta_o_espaco] + '\n' + self.wrap(text[onde_esta_o_espaco+1:])
