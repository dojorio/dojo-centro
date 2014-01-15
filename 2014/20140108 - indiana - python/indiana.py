def horizontais(rampas, largura):
    for i, rampa in enumerate(rampas):
        if i % 2 == 0:
            yield largura - rampa[1]
        else:
            yield rampa[1]

def verticais(rampas, largura):
    for i, rampa in enumerate(rampas[:-1]):
        if i % 2 == 0:
            pontos = (0, rampas[0], )
        else:
    yield 2000

def indiana(rampas, largura, altura):
    return min(
        min(horizontais(rampas, largura)),
        min(verticais(rampas, largura)))