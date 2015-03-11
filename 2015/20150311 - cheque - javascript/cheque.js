exports.porExtenso = function (numero) {
    var traducoes = ['','','dois','três','quatro','cinco',
                     'seis', 'sete', 'oito', 'nove', 'dez',
                     'onze', 'doze', 'treze', 'quatorze', 
                     'quinze', 'dezesseis', 'dezessete', 
                     'dezoito', 'dezenove', 'vinte'         ]

    if (numero === 1) {
        return 'um real'
    }

    return traducoes[numero] + ' reais'
}