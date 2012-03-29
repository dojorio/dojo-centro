def int2(numero):
    if numero == '': return 0
    return int(numero)

def avaliar(expressao):
    
    if expressao.isdigit():
        return int2(expressao)
    
    
    if '+' in expressao:
        return reduce(lambda a,b: a + b, map(avaliar, expressao.split('+')))

    if '-' in expressao:
        return reduce(lambda a,b: a - b, map(avaliar, expressao.split('-')))
    
    if '*' in expressao:
        return reduce(lambda a,b: a * b, map(avaliar, expressao.split('*')))

    
