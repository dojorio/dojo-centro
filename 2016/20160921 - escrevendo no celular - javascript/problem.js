var dict = {
	'ABC' : '2',
	'D' : '3'
}

var keys = Object.keys(dict)

function getCodeFromLetter (letter) {
	for (var i = 0; i < keys.length; i++){
		var regex = new RegExp('[' + keys[i] + ']')
		if(regex.test(letter)){
			return dict[keys[i]].repeat(keys[i].indexOf(letter) + 1)
		}

	}

	return '';
}

exports.problem = function (str) {

	if (str.length) {
		
		var ary = str.split('')
		var res = ''

		for (var j = 0; j < ary.length;j++){
			if(ary[j] === ary[j+1]){
				res += getCodeFromLetter(ary[j]) + "_" + getCodeFromLetter(ary[j+1])	
				return res
			}
		res += getCodeFromLetter(ary[j])

		}

		return res
		

	} 
	
	return ''





};
