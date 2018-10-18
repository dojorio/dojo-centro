exports.testRegex = function (input) {
	var rawExp = getExpression(input.exp)
	if (rawExp.indexOf('(') != -1) {
		// (a).(b)
		fRawExp = getExpression(rawExp)
		sRawExp = getExpression(rawExp.split('.'))
	}
	if (rawExp.indexOf('(') != -1) {
		rawExp = getExpression(rawExp)
	}

	if(rawExp.indexOf('*') != -1) {
		var char = rawExp.replace('*', '')
		var cChar = (char == 'a') ? 'b' : 'a'
		if(input.test.indexOf(cChar) == -1) {
			return 'Y'
		} else {
			return 'N'
		}
	}

	if(rawExp.indexOf('|') != -1) {
		var char = rawExp.split('|')
		if(char[0] == input.test || char[1] == input.test) {
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
	exp[0] = ''
	exp[exp.length - 1] = ''
	return exp.split('(')[1][exp.length - 1]
};