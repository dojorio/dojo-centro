def hora_binaria(hora, minuto):
    sufix = minuto % 2

    if minuto < 2:
        return ('0001','00000'+str(sufix))
    elif minuto == 2:
        return ('0001','000010')
    elif minuto == 3:
        return ('0001','000011')
