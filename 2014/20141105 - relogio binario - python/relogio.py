def hora_binaria(hora, minuto):
    bin_minuto = ''

    for i in range(0, 5):
        quociente = minuto // 2 ** i
        bin_minuto = str(quociente % 2) + bin_minuto

    return ('0001','0' + bin_minuto)

