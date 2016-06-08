def static numberOfMoves (source, target) {
	if (source == target) {
		return 0
	}

	if (source.length() == 3) {
		if(target[2] == 'n'){
			return 1
		}
		return 2
	}

	1
}