exports.testRegex = function (input) {
	var rawExp = getExpression(input.exp)
	if(rawExp.replace('.', '') == input.test) {
    	return 'Y'
    } else {
    	return 'N'
    }


};

function getExpression(exp) {
	return exp.split('(')[1].split(')')[0]
};