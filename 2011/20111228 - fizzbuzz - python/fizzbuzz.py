
def fizzbuzz (numero):
    resultado = ''
    if eh_divisivel_por_3(numero):
        resultado = 'Fizz'
    if eh_divisivel_por_5(numero):
        resultado = resultado + 'Buzz'

    if resultado == '':
        resultado = numero
    return resultado
    
def eh_divisivel_por_3(dividendo):
    return dividendo % 3 == 0
    
def eh_divisivel_por_5(dividendo):
    return dividendo % 5 == 0
 