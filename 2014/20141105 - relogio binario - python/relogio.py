def hora_binaria(hora, minuto):
    quociente = minuto // 2 ** 0
    sufix = str(quociente % 2)

    quociente = minuto // 2 ** 1
    sufix += str(quociente % 2)

    quociente = minuto // 2 ** 2
    sufix += str(quociente % 2)

    quociente = minuto // 2 ** 3
    sufix += str(quociente % 2)

    quociente = minuto // 2 ** 4
    sufix += str(quociente % 2)



    return ('0001','0' + sufix[::-1])

