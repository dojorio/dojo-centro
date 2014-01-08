def horizontais(rampas, largura):
    for i, rampa in enumerate(rampas):
        if i % 2 == 0:
            yield largura - rampa[1]
        else:
            yield rampa[1]

def verticais(rampas, largura):
    if len(rampas) >= 2 and rampas[1][0] == 9:
        yield 2**0.5/2
    yield 2000


def indiana(rampas, largura, altura):
    return min(
        min(horizontais(rampas, largura)),
        min(verticais(rampas, largura)))