def hora_binaria(hora, minuto):
    sufix = str(minuto % 2)
    quociente = minuto // 2
    sufix += str(quociente % 2)
    quociente = quociente // 2
    sufix += str(quociente % 2)
    
    return ('0001','000' + reversed(list(sufix)))

