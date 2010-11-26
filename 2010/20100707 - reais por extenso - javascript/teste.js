$(document).ready(function(){
    describe('Conversão de valores', {
        'Deve retornar um real ao receber "R$ 1,00"': function() {
            value_of(converte_valor_para_extenso('R$ 1,00')).should_be('um real');
        },
        'Deve retornar dois reais ao receber "R$ 2,00"': function() {
            value_of(converte_valor_para_extenso('R$ 2,00')).should_be('dois reais');
        },
        'Deve retornar três reais ao receber "R$ 3,00"': function() {
            value_of(converte_valor_para_extenso('R$ 3,00')).should_be('três reais');
        },
        'Deve retornar quatro reais ao receber "R$ 4,00"': function() {
            value_of(converte_valor_para_extenso('R$ 4,00')).should_be('quatro reais');
        },
        'Deve retornar cinco reais ao receber "R$ 5,00"': function() {
            value_of(converte_valor_para_extenso('R$ 5,00')).should_be('cinco reais');
        },
        'Deve retornar seis reais ao receber "R$ 6,00"': function() {
            value_of(converte_valor_para_extenso('R$ 6,00')).should_be('seis reais');
        },
        'Deve retornar sete reais ao receber "R$ 7,00"': function() {
            value_of(converte_valor_para_extenso('R$ 7,00')).should_be('sete reais');
        },
        'Deve retornar valor unitario de zero a 9 por extenso': function() {
            value_of(converte_valor_para_extenso('R$ 0,00')).should_be('zero reais');
            value_of(converte_valor_para_extenso('R$ 8,00')).should_be('oito reais');
            value_of(converte_valor_para_extenso('R$ 9,00')).should_be('nove reais');
        },

        'Deve retornar sete reais ao receber "R$ 10,00"': function() {
            value_of(converte_valor_para_extenso('R$ 10,00')).should_be('dez reais');
        },
        'Deve retornar valor por extenso de "R$ 11,00" a "R$ 20,00"': function() {
            value_of(converte_valor_para_extenso('R$ 11,00')).should_be('onze reais');
            value_of(converte_valor_para_extenso('R$ 12,00')).should_be('doze reais');
            value_of(converte_valor_para_extenso('R$ 13,00')).should_be('treze reais');
            value_of(converte_valor_para_extenso('R$ 14,00')).should_be('quatorze reais');
            value_of(converte_valor_para_extenso('R$ 15,00')).should_be('quinze reais');
            value_of(converte_valor_para_extenso('R$ 16,00')).should_be('dezesseis reais');
            value_of(converte_valor_para_extenso('R$ 17,00')).should_be('dezessete reais');
            value_of(converte_valor_para_extenso('R$ 18,00')).should_be('dezoito reais');
            value_of(converte_valor_para_extenso('R$ 19,00')).should_be('dezenove reais');
            value_of(converte_valor_para_extenso('R$ 20,00')).should_be('vinte reais');
        },

        'Deve retornar vinte e um ao receber "R$ 21,00"': function() {
            value_of(converte_valor_para_extenso('R$ 21,00')).should_be('vinte e um reais');
        },

    })
});

