module("Cheque");

test("Unidades", function(){
    equal(numeroPorExtenso(0), "zero");
    equal(numeroPorExtenso(1), "um");
    equal(numeroPorExtenso(2), "dois");
    equal(numeroPorExtenso(3), "três");
    equal(numeroPorExtenso(4), "quatro");
    equal(numeroPorExtenso(5), "cinco");
    equal(numeroPorExtenso(6), "seis");
    equal(numeroPorExtenso(7), "sete");
    equal(numeroPorExtenso(8), "oito");
    equal(numeroPorExtenso(9), "nove");   
});

test("Dezenas", function(){
    equal(numeroPorExtenso(10), "dez");
    
    equal(numeroPorExtenso(11), "onze");
    equal(numeroPorExtenso(12), "doze");
    equal(numeroPorExtenso(13), "treze");
    equal(numeroPorExtenso(14), "quatorze");
    equal(numeroPorExtenso(15), "quinze");
    equal(numeroPorExtenso(16), "dezesseis");
    equal(numeroPorExtenso(17), "dezessete");
    equal(numeroPorExtenso(18), "dezoito");
    equal(numeroPorExtenso(19), "dezenove");
    
    equal(numeroPorExtenso(20), "vinte");
    equal(numeroPorExtenso(30), "trinta");
    equal(numeroPorExtenso(40), "quarenta");
    equal(numeroPorExtenso(50), "cinquenta");
    equal(numeroPorExtenso(60), "sessenta");
    equal(numeroPorExtenso(70), "setenta");
    equal(numeroPorExtenso(80), "oitenta");
    equal(numeroPorExtenso(90), "noventa");
});

test("Dezenas compostas", function(){
    equal(numeroPorExtenso(21), "vinte e um");
    equal(numeroPorExtenso(22), "vinte e dois");
    equal(numeroPorExtenso(23), "vinte e três");
    equal(numeroPorExtenso(24), "vinte e quatro");
    equal(numeroPorExtenso(31), "trinta e um");
    equal(numeroPorExtenso(32), "trinta e dois");
    equal(numeroPorExtenso(41), "quarenta e um");
    equal(numeroPorExtenso(42), "quarenta e dois");
    equal(numeroPorExtenso(51), "cinquenta e um");
});

test("Centenas", function(){
    var tests = [
        [100, "cem"],
        [200, "duzentos"],
        [300, "trezentos"],
        [400, "quatrocentos"],
        [500, "quinhentos"],
        [600, "seiscentos"],
        [700, "setecentos"],
        [800, "oitocentos"],
        [900, "novecentos"],
    ];
                
    tests.forEach(function (t) {
        equal(numeroPorExtenso(t[0]), t[1]);
    });
});

test("Centenas composta", function(){
    var tests = [
        [101, "cento e um"],
        [102, "cento e dois"],
        [103, "cento e três"],
        [112, "cento e doze"],
        [173, "cento e setenta e três"],
        [222, "duzentos e vinte e dois"],
        [322, "trezentos e vinte e dois"],
        [422, "quatrocentos e vinte e dois"],
        [522, "quinhentos e vinte e dois"],
    ];
                
    tests.forEach(function (t) {
        equal(numeroPorExtenso(t[0]), t[1]);
    });
});

test("Milhares", function(){
    var tests = [
        [1000, "um mil"],
        [2000, "dois mil"],
        [3000, "três mil"],
        
        [1001, "um mil e um"],
        [1033, "um mil e trinta e três"],
        [1533, "um mil e quinhentos e trinta e três"],
        [4533, "quatro mil e quinhentos e trinta e três"],
    ];
                
    tests.forEach(function (t) {
        equal(numeroPorExtenso(t[0]), t[1]);
    });
});

