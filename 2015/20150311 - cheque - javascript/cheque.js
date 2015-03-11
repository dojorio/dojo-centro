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

    } else {
        return 'vinte e ' + traducoes[numero.toString()[1]] + ' reais'
    }
}