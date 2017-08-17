def static catTaro(string) {

	string = string.replace('B', '')

	if (string.contains ('CAT') &&
		string.count('C') == 1 &&
		string.count('A') == 1 &&
		string.count('T') == 1) {
		return 'Possible'
	}

	return 'Impossible'
}
