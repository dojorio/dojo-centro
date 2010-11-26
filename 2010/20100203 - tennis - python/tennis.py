
class Game():
    JOGADOR1 = 0
    JOGADOR2 = 1
    VALORES_DO_PLACAR = [0, 15, 30, 40]
    
    def __init__(self, pontos1=0, pontos2=0):
        self._pontos = [
            self.p2i(pontos1),
            self.p2i(pontos2)
        ]

    @property
    
    def placar(self):
        placar1 = self.VALORES_DO_PLACAR[self._pontos[0]]
        placar2 = self.VALORES_DO_PLACAR[self._pontos[1]]
        return placar1, placar2
        
    def pontua(self, jogador):
        self._pontos[jogador] += 1

    def p2i(self, ponto):
        """
        recebe um ponto e retorno o indice correspondente 
        no VALORES_DO_PLACAR
        """
        return self.VALORES_DO_PLACAR.index(ponto)
    