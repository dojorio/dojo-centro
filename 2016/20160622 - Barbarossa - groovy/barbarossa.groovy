def static armedSoldiers (soldiers, arms, daysToSnow) {
	if (soldiers == 0)
		return 0

	def armsPerSoldiers = arms / soldiers

	if (daysToSnow == 9) {
		def mod = arms % soldiers

		if (armsPerSoldiers >= 3){
			return soldiers
		} else {
			return arms%soldiers
		}
	} else if (daysToSnow == 11) {
		def mod = arms % soldiers

		if (armsPerSoldiers >= 1) {
			return soldiers 
		} else {
				return mod 
		}
	}

	arms ? soldiers : 0
}