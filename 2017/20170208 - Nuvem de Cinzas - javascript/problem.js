exports.problem = function (map) {
    if (!map[0].includes('A')) {
    	return 0
    } 

    var pos_aster = map[0].search(/\*/)
    var pos_A = map[0].search("A")

    return pos_A - pos_aster
    
};
