def static catTaro(string) {
	string = string.replaceAll(/[^CAT]/, '')

	return string == 'CAT' ? 'Possible' : 'Impossible'
}
