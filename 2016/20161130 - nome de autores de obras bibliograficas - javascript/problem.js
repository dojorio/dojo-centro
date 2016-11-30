exports.nomeAutor = function (nome) {
  
  // array

  if (nome.includes(' ')){
  	nome = nome.split(' ')
  	sobrenome = nome[1]
  	nome = nome[0]
  	sobrenome.toUpperCase()
    nome[0].toUpperCase()
  	return sobrenome + ', ' + nome;
  	}
  return nome.toUpperCase()

};
