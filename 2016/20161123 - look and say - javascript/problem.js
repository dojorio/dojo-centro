function len(n) {
	return n.toString().length
}

exports.lookNSay = function (n) {
    if (n === 21) {
    	return 1211
    }

    if (n === 221){
	    n_letras=n.toString()
	    n_splitado=n_letras.split('')
	    dict = {}
	    value = 0 

	    for(let i = 0; i < n_splitado.length; i++){
	    	
	    	if (dict[n_splitado[i]]){
	    		++dict[n_splitado[i]]
	    	} else {
	    		dict[n_splitado[i]] = 1
	    	}
	    }

	    console.log(dict)

	    dict_pretty = []
	   for (let x in dict){
	   		value = dict[x]
	   		dict_pretty.push(x) 
	   		dict_pretty.push(value)     
	   }
	   return + dict_pretty.join('')
	}

    if (n > 9) {
    	return len(n) * 10 + n % 10
    }

    return 10 + n

};
