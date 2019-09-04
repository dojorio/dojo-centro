exports.encontreOTelefone = function (param) {

	if (param == 'D' || param == 'E' || param == 'F') {
		return 3
	};

	if (param == 'G' || param == 'H') {
		return 4
	};

    return 2
};
