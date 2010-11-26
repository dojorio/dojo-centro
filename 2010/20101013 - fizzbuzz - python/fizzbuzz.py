def fizzbuzz(numero):
    resultado = ''
    if numero % 3 == 0:
        resultado += 'fizz'

    if numero % 5 == 0:
        resultado += 'buzz'

    if len(resultado) == 0:
        return str(numero)

    return resultado

