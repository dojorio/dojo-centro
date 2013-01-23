NUMEROS = {
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
    14 => 'quatorze',
    15 => 'quinze',
    16 => 'dezesseis',
    17 => 'dezessete',
    18 => 'dezoito',
    19 => 'dezenove',
    20 => 'vinte',
    30 => 'trinta',
    40 => 'quarenta',
    50 => 'cinquenta',
    60 => 'sessenta',
    70 => 'setenta',
    80 => 'oitenta',
    90 => 'noventa',
    100 => 'cem',
    200 => 'duzentos',
    300 => 'trezentos',
    400 => 'quatrocentos',
    500 => 'quinhentos',
    600 => 'seiscentos',
    700 => 'setecentos',
    800 => 'oitocentos',
    900 => 'novecentos',
    1000 => 'mil'
}

def extenso(numero)

    return NUMEROS[numero] if NUMEROS[numero]

    if numero < 100
        return extenso((numero/10)*10) + ' e ' + extenso(numero % 10)
    elsif numero < 200
        return 'cento e ' + extenso(numero % 100)
    elsif numero < 1000 
        return extenso((numero/100)*100) + ' e ' + extenso(numero % 100)
    else
        if (numero % 1000)/100 == 1
            return extenso((numero/1000)*1000)+ " " +extenso(numero % 1000)
        elsif (numero % 1000)/100 == 2
            return extenso((numero/1000)*1000)+ " " +extenso(numero % 1000)
        else  
            return extenso((numero/1000)*1000)+ ' e ' + extenso(numero % 1000)
        end
    end    
end