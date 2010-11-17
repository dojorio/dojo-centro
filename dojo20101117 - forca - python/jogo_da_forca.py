class JogoDaForca:
    def __init__(self, palavra, numero_maximo_de_erros):
        self.palavra = palavra
        self.ganhou = False
        self.erros = 0

    def tentativa(self, letra):
        self.ganhou = letra == self.palavra
        if not self.ganhou:
            self.erros += 1
        return self

