exports.porExtenso = function (numero) {
    var traducoes = ['','um','dois','três','quatro','cinco',
                     'seis', 'sete', 'oito', 'nove', 'dez',
                     'onze', 'doze', 'treze', 'quatorze', 
                     'quinze', 'dezesseis', 'dezessete', 
                     'dezoito', 'dezenove', 'vinte'         ]

    if (numero === 1) {
        return 'um real'
    }

    if(numero <= 20){
        return traducoes[numero] + ' reais'
    }

    if(numero < 30){
        return 'vinte e ' + traducoes[numero.toString()[1]] + ' reais'
    }

    if(numero === 30){
        return 'trinta reais'
    }

    return 'trinta e ' + traducoes[numero.toString()[1]] + ' reais'
}