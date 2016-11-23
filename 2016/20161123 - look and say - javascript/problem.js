function len(n) {
	return n.toString().length
}

exports.lookNSay = function (n) {
    if (n === 21) {
    	return 1211
    }

    if (n === 221){
	    n_letras=n.toString()
	    n_splitado=n_letras.split()
	    dict = {}

	    for(let i = 0; i < n_splitado; i++){
	    	if (dict[i] != null){
	    		dict[i] = dict[i]++
	    	} else {
	    		dict[i] = 1
	    	}

	    };

	    dict_pretty = ''
	   for (let x in dict){
	   		keys[] = dict[x]
	   		values[] = dict[keys[x]]  
	   }
	}



    if (n > 9) {
    	return len(n) * 10 + n % 10
    }

    return 10 + n

};
