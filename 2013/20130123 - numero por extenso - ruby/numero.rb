def extenso(numero)
    numeros = {
        1 => 'um',
        2 => 'dois',
        3 => 'três',
        4 => 'quatro',
        5 => 'cinco',
        6 => 'seis',
        7 => 'sete',
        8 => 'oito',
        9 => 'nove',
        10 => 'dez',
        11 => 'onze',
        12 => 'doze',
        13 => 'treze',
        14 => 'quartoze',
        15 => 'quinze',
        16 => 'dezesseis',

    }
    if numeros[numero]
        return numeros[numero]
    else
        return "onze"
    end 

end