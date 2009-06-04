var Ambiente = function(){
    var ambiente = this;
    this.conteudo = [];
    this.inserir = function(o_que){
        o_que.inserir_se(ambiente);
    };
    this.propagar = function(o_que){
        ambiente.conteudo[0].ouvir(o_que);
    };
};

var DonaChica = function(){
    var $this = this;
    this.admirada = false;
    this.inserir_se = function(onde){
        onde.conteudo.push($this);
    };
    this.ouvir = function(som){
        $this.admirada = true;
    }
};

var Gato = function(){
    var $this = this;
    this.vivo = true;
    this.ambiente = null;
    this.berrar = function(){
        var berro = new Berro();
        berro.origem = $this;
        if (this.ambiente != null) {
            this.ambiente.propagar(berro);
        }
    };
    this.inserir_se = function(onde){
        onde.conteudo.push(this);
        this.ambiente = onde;
    };
};

var Cao = function(){
    var $this = this;
    this.ambiente = null;
    this.berrar = function(){};
    this.inserir_se = function(onde){
        onde.conteudo.push(this);
        this.ambiente = onde;
    };
};

var Berro = function(){
    this.origem = null;
};

var Pau = function(){};

var atira = function(o_que, em_quem){
    em_quem.berro = true;
};

var morto = function (ser){
    return !ser.vivo;
};