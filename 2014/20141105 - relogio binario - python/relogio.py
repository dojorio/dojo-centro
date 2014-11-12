


def _binarizator(numero, qtd_de_bits):
    bin = ''
    for i in range(0, qtd_de_bits):
        quociente = numero // 2 ** i
        bin = str(quociente % 2) + bin
    return bin


def hora_binaria(hora, minuto):
    bin_hora = _binarizator(hora, 4)
    bin_minuto = _binarizator(minuto, 6)

    return (bin_hora, bin_minuto)

