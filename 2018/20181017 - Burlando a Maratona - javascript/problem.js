exports.testRegex = function (input) {
	if (getExpression(input.exp) == input.test) {
    	return 'Y'
    } else {
    	return 'N'
    }


};

function getExpression(exp) {
	return exp.split('(')[1].split(')')[0]
};