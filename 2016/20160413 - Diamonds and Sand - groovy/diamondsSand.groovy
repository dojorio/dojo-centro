def static pan (mine) {
	mine = mine.replace('.', '')

	def result = 0

	while (mine.contains('<>')) {
		result += mine.count('<>')
		mine = mine.replace('<>', '') 
	}

	return result
}
