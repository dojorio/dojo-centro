'use strict';

exports.nomeAutor = function (nome) {

  if (nome.includes(' ')) {

  	let lista = nome.split(' ')
  	let sobrenome = lista[lista.length - 1].toUpperCase()
  	let prenome = lista
  		.slice(0, lista.length - 1)
  		.map(n => {

  			if (['da', 'das', 'do', 'dos', 'de'].includes(n)) return n

  			return n.charAt(0).toUpperCase() +
  				n.substring(1).toLowerCase()
  		})
  		.join(' ')
  	
  	return sobrenome + ', ' + prenome 
  }
  
  return nome.toUpperCase()

};
