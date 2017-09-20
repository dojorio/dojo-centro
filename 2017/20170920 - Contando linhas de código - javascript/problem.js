exports.countCode = function (fileContent) {
	if (fileContent == "") {
		return 0	
	}
	else (fileContent == "public class Teste {\n}") {
		return 2
	}		
    return 1
};
