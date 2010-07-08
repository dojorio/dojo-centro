function tratar_cifra_para_reais(reais){
    var cifra = " reais";
    if (reais == 1){
        cifra = " real";
    };
    return cifra;
}

function converte_valor_para_extenso(valor)
{

    var dicionario = {
        0: "zero",
        1: "um",
        2: "dois",
        3: "três",
        4: "quatro",
        5: "cinco",
        6: "seis",
        7: "sete",
        8: "oito",
        9: "nove",
        10: "dez",
        11: "onze",
        12: "doze",
        13: "treze",
        14: "quatorze",
        15: "quinze",
        16: "dezesseis",
        17: "dezessete",
        18: "dezoito",
        19: "dezenove",
        20: "vinte"
    };

    valor = valor.replace("R$ ", "").replace(",00", "");

    if(valor > 20){
        return dicionario[20] + " e " + dicionario[valor[1]] + tratar_cifra_para_reais(valor);
    }

    return dicionario[valor] + tratar_cifra_para_reais(valor);
}

