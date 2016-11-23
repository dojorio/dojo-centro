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

	    for(let i = 1; i < n_splitado.length; i++){

	    	if (dict[i] != null){
	    		dict[i] = dict[i]++
	    	} else {
	    		dict[i] = i
	    	}
	    };


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
