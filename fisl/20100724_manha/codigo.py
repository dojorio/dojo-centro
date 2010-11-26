def triangulo(lado1, lado2, lado3):

    ladoMaior = max(lado1, lado2, lado3)
    listaLados = [lado1, lado2, lado3]
    listaLados.sort
    listaLados.pop

    if lado2 > (lado1 + lado3) or lado1 > (lado2 + lado3) or lado3 > (lado1 + lado2) or lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        return "invalido"
    
    else:
    
        if lado1 == lado2 == lado3:
            return "equilatero"
    
        if lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
            return "isosceles"
