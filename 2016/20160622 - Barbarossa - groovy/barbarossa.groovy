def static armedSoldiers (soldiers, arms, daysToSnow) {
	if (daysToSnow == 9)
		return (arms == 3 ? 1 : 0)
	arms ? soldiers : 0
}