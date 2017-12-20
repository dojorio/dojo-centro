def static efeitoMagnetico (magnetos, cursor) {
	def magneto = magnetos[0]

	if (magneto == [] | magneto[0] != cursor[0] || cursor[1] != magneto[1]) {
		return cursor
	}

	magneto[0..1]
}
