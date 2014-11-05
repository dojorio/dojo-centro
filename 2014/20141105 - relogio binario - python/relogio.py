def hora_binaria(hora, minuto):
    bin_minuto = ''
    bin_hora = ''

    for i in range(0, 2):
        quociente = hora // 2 ** i
        bin_hora = str(quociente % 2) + bin_minuto

    for i in range(0, 6):
        quociente = minuto // 2 ** i
        bin_minuto = str(quociente % 2) + bin_minuto

    return ('00' + bin_hora, bin_minuto)

