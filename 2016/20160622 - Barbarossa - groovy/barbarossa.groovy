def static armedSoldiers (soldiers, arms, daysToSnow) {

	if (daysToSnow == 9) {

		def armsPerSoldiers = arms/soldiers
		def mod = arms%soldiers

		return (armsPerSoldiers + mod > 2 ? 1 : 0)
	}

	arms ? soldiers : 0
}