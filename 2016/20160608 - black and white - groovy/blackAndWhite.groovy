def static numberOfMoves (source, target) {
	def total = 0, found = false

	source.eachWithIndex { letter, index ->
		if (letter != target[index]) {
			total += found ? 0 : 1
			found = true
		} else {
			found = false
		}
	}

	return total
}