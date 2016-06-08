def static numberOfMoves (source, target) {
	def total = 0,
	    found = false

	source.eachWithIndex { letter, index ->
		if (letter != target[index]) {
			total += found ? 1 : 0
			found = false
		} else {
			found = true
		}

	}

	return total == source.length() ? 1 : total
}