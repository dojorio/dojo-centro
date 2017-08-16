def static catTaro(string) {
	if (string.contains ('CAT') &&  string.count('C') == 1 && string.count('T') == 1 ) {
		return 'Possible'
	}
	return 'Impossible'
}
