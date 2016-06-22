def static armedSoldiers (soldiers, arms, daysToSnow) {

	if (daysToSnow == 9) {
		def armsPerSoldiers = arms/soldiers
		def mod = arms%soldiers

		if (mod == 0) {
			return armsPerSoldiers > 2 ? soldiers : 0
		} else {
			return armsPerSoldiers == 2 ? mod : 0
		}
	}

	arms ? soldiers : 0
}