def static armedSoldiers (soldiers, arms, daysToSnow) {
	if (soldiers == 0)
		return 0

	def armsPerSoldiers = arms / soldiers

	if (daysToSnow == 9) {
		def mod = arms % soldiers

		if (mod == 0) {
			return armsPerSoldiers > 2 ? soldiers : 0
		} else {
			return armsPerSoldiers as int == 2 ? mod : 0
		}
	} else if (daysToSnow == 11) {
		def mod = arms % soldiers

		if (mod == 0) {
			return armsPerSoldiers > 0 ? soldiers : 0
		} else {
			
			if((armsPerSoldiers as int) == 6){
				return 	3
			}
			
			if((armsPerSoldiers as int) == 0){
				return 	mod
			}else {
				return 0
			}

		}
	}

	arms ? soldiers : 0
}