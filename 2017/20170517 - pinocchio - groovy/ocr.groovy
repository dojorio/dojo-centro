def static problem (pinocchio1, pinocchio2, pista) {
	def p1 = pinocchio1.sum()
	def p2 = pinocchio2.sum()
	if(p1 > p2) 
        return "pinocchio1" 

    else if(p2 > p1) 
        return "pinocchio2"

    else
        return "empate"

}
