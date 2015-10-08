def fail(initial_house, drunks_house, tries, probabilities):
	if drunks_house == None:
	    return 1

	if initial_house == drunks_house:
		return 0
	else:

		return 1 - probabilities[initial_house][drunks_house]