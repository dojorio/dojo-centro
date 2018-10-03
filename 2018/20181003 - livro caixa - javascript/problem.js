exports.box_book = function (total, list) {
	function add ( a, b){
		return a + b
	}
	if (total < 0) {
		return '-' 
	}
 	if ( list.reduce(add, 0) === total) { 
 		var str = ''
 		for (var i = list.length - 1; i >= 0; i--) {
 			str = str+'+'
 		}
 		return str	
 	}
 	if (list[0] < total || list[0] > total){
 		return '*'
 	}

    return '+'
}


