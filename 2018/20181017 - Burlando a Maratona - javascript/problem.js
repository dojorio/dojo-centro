exports.testRegex = function (input) {
	var rawExp = getExpression(input.exp)

	if(rawExp.indexOf('*') != -1) {
		var char = rawExp.replace('*', '')
		var cChar = (char == 'a') ? 'b' : 'a'
		console.log(input.test.indexOf(cChar))
		if(input.test.indexOf(cChar) != -1) {
			return 'Y'
		} else {
			return 'N'
		}
	}

	if(rawExp.replace('.', '') == input.test) {
    	return 'Y'
    } else {
    	return 'N'
    }


};

function getExpression(exp) {
	return exp.split('(')[1].split(')')[0]
};