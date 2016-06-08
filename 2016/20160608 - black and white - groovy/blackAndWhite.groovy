def static numberOfMoves (source, target) {
	def total = 0

	source.eachWithIndex { letter, index ->
		total += letter == target[index] ? 0 : 1
	}

	return total == source.length() ? 1 : total
}