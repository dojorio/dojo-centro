def fail(initial_house, drunks_house, tries, probabilities):
	if initial_house == drunks_house:
		return 0
	else:
		return probabilities[initial_house][0]