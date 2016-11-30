'use strict';

exports.nomeAutor = function (nome) {

  if (nome.includes(' ')) {

  	let lista = nome.split(' ')

  	let eJunior =  lista[lista.length - 1] === 'Junior' 

  	let sobrenome = eJunior ?
  		lista[lista.length - 2] + ' ' + lista[lista.length - 1] :
  	  lista[lista.length - 1]

  	let prenome = lista.slice(0, lista.length - (eJunior ? 2 : 1)) 
  		.map(n => {

  			if (['da', 'das', 'do', 'dos', 'de'].includes(n)) return n

  			return n.charAt(0).toUpperCase() +
  				n.substring(1).toLowerCase()
  		})
  		.join(' ')
  	
  	return sobrenome.toUpperCase() + ', ' + prenome 
  }
  
  return nome.toUpperCase()

};
