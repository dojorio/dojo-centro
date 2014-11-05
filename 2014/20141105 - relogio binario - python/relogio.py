def hora_binaria(hora, minuto):
    sufix = str(minuto % 2)
    quociente = minuto // 2
    sufix2 = str(quociente % 2)

    
    return ('0001','0000' + sufix2 + sufix)

