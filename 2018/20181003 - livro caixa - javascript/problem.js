exports.box_book = function (total, list) {
	function add ( a, b){
		return a + b
	}
	function sub (a,b){
		return a - b
	}
 	if ( list.reduce(sub, 0) === total) { 
 		var str = ''
 		for (var i = list.length - 1; i >= 0; i--) {
 			str = str+'-'
 		}
 		return str		
 	}

 	if (list.length == 1){
 		if(list[0] < total || list[0] > total){
 			return '*'
 		}
 	}

 	if ( list.reduce(add, 0) === total) { 
 		var str = ''
 		for (var i = list.length - 1; i >= 0; i--) {
 			str = str+'+'
 		}
 		return str	
 	}

    return '-+'
}


