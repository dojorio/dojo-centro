var dict = {
	'ABC' : '2',
	'DEF' : '3',
	'GHI' : '4',
	'JKL' : '5',
	'MNO' : '6',
	'PQRS' : '7',
	'TUV' : '8',
	'WXYZ' : '9',
	' ' : '0'
}

var keys = Object.keys(dict)

function getCodeFromLetter (letter, next) {
	for (var i = 0; i < keys.length; i++){
		if(keys[i].indexOf(letter) > -1){

			var append = keys[i].indexOf(next) > -1 ? '_' : ''

			return dict[keys[i]]
				.repeat(keys[i].indexOf(letter) + 1) +
				append
		}

	}

	return '';
}

exports.problem = function (str) {

	if (str.length) {
		
		var arr = str.split('')

		return arr.reduce(function (acc, letter, i) {
			return acc + getCodeFromLetter(letter, arr[i+1])
		}, '')
		

	} 
	
	return ''





};
