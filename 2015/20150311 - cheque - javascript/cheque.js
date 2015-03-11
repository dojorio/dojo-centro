exports.porExtenso = function (numero) {
    var traducoes = ['','','dois','três','quatro','cinco']

    if (numero === 1) {
        return 'um real'
    }

    return traducoes[numero] + ' reais'
}