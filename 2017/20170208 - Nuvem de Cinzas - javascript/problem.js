exports.problem = function (map) {
    if (!map[0].includes('A')) {
    	return 0
    } 
    var posAeroporto = map[0].search("A")


    var posFumaca = map[0].search(/\*/)
    var posAeroporto = map[0].search("A")

    return posAeroporto - posFumaca

    
};
