'use strict';

exports.nomeAutor = function (nome) {

  if (nome.includes(' ')) {

  	let lista = nome.split(' ')
  	let sobrenome = lista[1].toUpperCase()
  	let prenome = lista[0]
  	
  	return sobrenome +
  		', ' + prenome.charAt(0).toUpperCase() +
  		prenome.substring(1);
  	
  }
  
  return nome.toUpperCase()

};
