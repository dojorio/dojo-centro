def static problem (pinocchio1, pinocchio2, pista) {

	def v1 = 5/pinocchio1[0]
	def v2 = 5/pinocchio2[0]

	def d1 = pista - pinocchio1[1]
	def d2 = pista - pinocchio2[1]

	def t1 = d1/v1
	def t2 = d2/v2

	if (t1 > t2)
		return "pinocchio2"
	else if (t1 < t2)
		return "pinocchio1"
	else
		return "empate"
}
