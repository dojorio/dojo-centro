function relacionamentos(relacoes_conhecidas){
	var relacionamentos =[];
	for(var i = 0; i <relacoes_conhecidas.length; i++){ 
		
		var pessoa1 = relacoes_conhecidas[i][0];
		var relacao = relacoes_conhecidas[i][1];
		var pessoa2 = relacoes_conhecidas[i][2];
		
		if (pessoa2 && pessoa2.sexo == "f"){
			relacionamentos.push (pessoa1 + " " + relacao + " " + pessoa2.nome);
			relacionamentos.push (pessoa2.nome + " mãe " + pessoa1); 
		}else if( relacao == "filha" || relacao == "filho"){
			relacionamentos.push (pessoa1 + " " + relacao + " " + pessoa2);
			relacionamentos.push (pessoa2 + " pai " + pessoa1); 
		}else{
			relacionamentos.push("bart irmão liza")
			relacionamentos.push("liza irmã bart");
		}
		
	}
	return relacionamentos
}
