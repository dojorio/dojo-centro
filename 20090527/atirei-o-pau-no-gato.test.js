$(function(){
module("Atirei o pau no gato");

test("Atirar o pau", function(){
    pau = new Pau();
    gato = new Gato();
    atira(pau, gato);
    ok(!morto(gato), "nenhum animal foi ferido durante o dojo");
    //equals(gato.vivo, 'a')
});

test("Dona Chica admirou-se", function(){
    dona_chica = new DonaChica();
    gato = new Gato();
    ambiente = new Ambiente();
    ambiente.inserir(dona_chica);
    ambiente.inserir(gato);
    
    ok(!dona_chica.admirada, "Dona Chica inicialmente não admirada");
    
    gato.berrar();
    
    ok(dona_chica.admirada, "Dona Chica ficou admirada");
});

test("Dona Chica nao ouviu o outro gato", function(){
    dona_chica = new DonaChica();
    gato = new Gato();
    gato_de_fora = new Gato();
    ambiente = new Ambiente();
    ambiente.inserir(dona_chica);
    ambiente.inserir(gato);
    
    ok(!dona_chica.admirada, "Dona Chica inicialmente não admirada");
    
    gato_de_fora.berrar();
    
    ok(!dona_chica.admirada, "Dona Chica nao ficou admirada");
});

test("Dona Chica não admirou-se com o berro do cão", function(){
    dona_chica = new DonaChica();
    gato = new Gato();
    cao = new Cao();
    ambiente = new Ambiente();
    ambiente.inserir(dona_chica);
    ambiente.inserir(gato);
    ambiente.inserir(cao);
    
    ok(!dona_chica.admirada, "Dona Chica inicialmente não admirada");
    
    cao.berrar();
    
    ok(!dona_chica.admirada, "Dona Chica não ficou admirada");
});

module("O pulo do gato!");

test("Gato insere-se em ambiente", function(){
    gato = new Gato();
    ambiente = new Ambiente();
    ambiente.inserir(gato);
    equals(gato.ambiente, ambiente, "O gato conhece seu ambiente");
    equals(ambiente.conteudo[0], gato, "O gato esta na area");
});

});