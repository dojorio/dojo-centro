def static armedSoldiers (soldiers, arms, daysToSnow) {
	if (daysToSnow == 9) {

		return ((arms == 5) || arms >= 3 && soldiers == 1 ? 1 : 0)
	}

	arms ? soldiers : 0
}