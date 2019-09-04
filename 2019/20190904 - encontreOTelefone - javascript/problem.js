exports.encontreOTelefone = function encontreOTelefone(param) {

	if (param == 'D' || param == 'E' || param == 'F') {
		return 3
	};

	if (param == 'G' || param == 'H' || param == 'I') {
		return 4
	};

	if (param == 'EI') {
		return encontreOTelefone('E') + encontreOTelefone('I');
	}

    return 2
};
