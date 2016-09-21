exports.problem = function (str) {
	
	

	if (str.length) {
		var dict = {
			'ABC' : '2',
			'D' : '3'
		}

		var keys = Object.keys(dict)
		var ary = str.split('')
		var res = []
		for (var j = 0; j < ary.length;j++){
			var letter = ary[j]
			for (var i = 0; i < keys.length; i++){
				var regex = new RegExp('[' + keys[i] + ']')
				if(regex.test(letter)){
					res.push(dict[keys[i]].repeat(keys[i].indexOf(letter) + 1))
				}

			}

		}

		return res.join('')
		

	} 
	
	return ''





};
