def hora_binaria(hora, minuto):
    sufix = str(minuto % 2)

    if minuto < 2:
        return ('0001','00000' + sufix)
    else:
        return ('0001','00001' + sufix)

