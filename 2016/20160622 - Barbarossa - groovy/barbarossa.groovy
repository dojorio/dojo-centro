def static armedSoldiers (soldiers, arms, daysToSnow) {

	def armsPerSoldiers = soldiers == 0 ? 0: arms / soldiers

	if (daysToSnow == 9) {
		
		def mod = arms % soldiers

		if (mod == 0) {
			return armsPerSoldiers > 2 ? soldiers : 0
		} else {
			return armsPerSoldiers as int == 2 ? mod : 0
		}
	}else if (daysToSnow == 11) {

		return armsPerSoldiers > 0 ? [arms, soldiers].min() : 0
	}

	arms ? soldiers : 0
}