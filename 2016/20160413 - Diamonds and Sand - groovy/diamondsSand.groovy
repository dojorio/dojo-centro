def static pan (mine) {
	mine = mine.replace('.', '')

	return mine.contains('<>') ? mine.count('<>') : 0
}
