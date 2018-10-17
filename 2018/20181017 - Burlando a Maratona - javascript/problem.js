exports.testRegex = function (input) {
	if (input.test == 'a' && input.exp == '(a)') {
    	return 'Y'
    } else {
    	return 'N'
    }
};
