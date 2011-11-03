def contar(numero)
    (1..numero).inject(0) do |soma, num|
        soma + numero_por_extenso(num).size
    end
end

def numero_por_extenso(numero)
    dicionario = {
        1 => 'um', 
        2 => 'dois', 
        3 => 'tres', 
        4 => 'quatro', 
        5 => 'cinco',
        6 => 'seis',
        7 => 'sete',
        8 => 'oito',
        9 => 'nove',
        10 => 'dex',
        11 => 'once',
        12 => 'doze',
        13 => 'treze',
        30 => 'trinta',
    }
    extenso = dicionario[numero]
    if extenso.nil?
        return 'vinte e ' + dicionario[numero % 10]
    else
        extenso
    end
end

def numero_letras(numero)
    numero_por_extenso(numero).gsub(' ', '').size
end

