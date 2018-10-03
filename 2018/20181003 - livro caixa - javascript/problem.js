exports.box_book = function (total, list) {
	function add ( a, b){
		return a + b
	}
	if (total < 0) {
		return '-' 
	}
 	if (list[0] < total){
 		return '*'
 	}
 	if ( list.reduce(add, 0) === total) { 
 		return '++'	
 	}

    return '+'
}


