def hora_binaria(hora, minuto):
    sufix = str(minuto % 2)
    quociente = minuto // 2
    sufix += str(quociente % 2)
    quociente = minuto // 4
    sufix += str(quociente % 2)

    quociente = minuto // 8
    sufix += str(quociente % 2)


    return ('0001','00' + sufix[::-1])

