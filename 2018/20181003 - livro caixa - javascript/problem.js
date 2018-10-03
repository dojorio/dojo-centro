exports.box_book = function (total, list) {
	if (total < 0) {
		return '-'
	}
 	if (list[0] < total){
 		return '*'
 	}
 	 	if ( list.reduce(add, 0) 
 		return '++'	
 	}

    return '+'
}


