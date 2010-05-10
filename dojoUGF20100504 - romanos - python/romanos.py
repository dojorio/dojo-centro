def romanos(numero_romano):
    valores = {
    'I' : 1,
    'V' : 5
    } 
    decimal = 0
    
    for caracter in numero_romano:
        if caracter == 'I':
            decimal = decimal + valores[caracter]

        else:
            decimal = valores[caracter] - decimal
    return decimal
