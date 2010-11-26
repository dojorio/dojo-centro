$(function(){
module("Relacionamento");

test("Bart é irmão de Liza então Liza é irmã de Bart", function(){
	var relacoes_conhecidas = [["bart", "irmão", "liza"]]
	isSet(relacionamentos(relacoes_conhecidas),
	["bart irmão liza", "liza irmã bart"], "Relacionamento possível") 	
});

test("Liza é irmã de Bart então Bart é irmão de Liza", function(){
	var relacoes_conhecidas = [["liza", "irmã", "bart"]]
	isSet(relacionamentos(relacoes_conhecidas),
	["bart irmão liza", "liza irmã bart"], "Relacionamento possível") 
});
	
test("Liza é filha de Homer então Homer é pai de Liza", function(){
	var relacoes_conhecidas = [["liza", "filha", "homer"]]
	isSet(relacionamentos(relacoes_conhecidas),
	["liza filha homer", "homer pai liza"], "Relacionamento possível") 
});

test("Bart é filho de Homer então Homer é pai de Bart", function(){
	var relacoes_conhecidas = [["bart", "filho", "homer"]]
	isSet(relacionamentos(relacoes_conhecidas),
	["bart filho homer", "homer pai bart"], "Relacionamento possível") 
});

test("Bart é filho de Marge então Marge é mãe de Bart", function(){
	var marge = {
		nome: "marge",
		sexo: "f"
	};
	var relacoes_conhecidas = [["bart", "filho", marge]]
	isSet(relacionamentos(relacoes_conhecidas),
	["bart filho marge", "marge mãe bart"], "Relacionamento possível") 
});
test("Bart e Liza são filhos de Homer, então Homer é pai de Bart e Liza e Bart e e Liza são irmãos", function(){
	var relacoes_conhecidas = [["bart", "filho", "homer"], ["liza", "filha", "homer"]]
	isSet(relacionamentos(relacoes_conhecidas),
	["bart filho homer", "homer pai bart", "liza filha homer", "homer pai liza", "bart irmão liza", "liza irmã bart"], "Relacionamento possível") 
});	
});
