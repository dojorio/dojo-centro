exports.countCode = function (fileContent) {
	if (fileContent == "") {
		return 0	
	}
	else {
		return fileContent.split("\n").length
	}		
    return 1
};
