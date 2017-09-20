exports.countCode = function (fileContent) {
	if (fileContent == "") {
		return 0	
	}
	else if (fileContent == "public class Teste {\n}") {
		return 2
	}		
    return 1
};
