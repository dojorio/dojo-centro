class JogoDaForca:
    def __init__(self, palavra):
        self.palavra = palavra
        self.erros = 0
        self.mascara = ['-'] * len(self.palavra)

    def __str__(self):
        return ''.join(self.mascara)

    @staticmethod
    def _atualiza_letra(letra1, letra2, mascara):
        if letra1 == letra2:
            return letra1
        else:
            return mascara


    def tente(self, letra):
        self.mascara = map(self._atualiza_letra, self.palavra, [letra] * len(self.palavra), self.mascara)
        if letra not in self.palavra:
            self.erros += 1

