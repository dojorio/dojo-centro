def static armedSoldiers (soldiers, arms, daysToSnow) {
	if (soldiers == 0)
		return 0

	def armsPerSoldiers = arms / soldiers

	if (daysToSnow >= 12 - armsPerSoldiers) {
		return soldiers
	}

	arms % soldiers
}