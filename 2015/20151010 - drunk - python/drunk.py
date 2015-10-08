def fail(initial_house, drunks_house, tries, probabilities):
	if tries < 1 or drunks_house == None:
	    return 1

	fail_on_this_try = 1 - probabilities[initial_house][drunks_house]

	return fail_on_this_try * fail(initial_house, drunks_house, tries - 1, probabilities)