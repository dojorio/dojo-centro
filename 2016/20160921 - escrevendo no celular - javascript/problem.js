exports.problem = function (str) {
	
	if (str.length) {
		var dict = {
			'ABC' : '2',
			'D' : '3'
		}

		var keys = Object.keys(dict)
		
		for (var i = 0; i < keys.length; i++){
			var regex = new RegExp('[' + keys[i] + ']')
			if(regex.test(str)){
				return dict[keys[i]].repeat(keys[i].indexOf(str) + 1)		
			}
			
		}

	} 
	
	return ''





};
