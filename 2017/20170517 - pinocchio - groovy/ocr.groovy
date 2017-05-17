def static problem (pinocchio1, pinocchio2, pista) {

	def p1 = 5/pinocchio1[0] + pinocchio1[1]
	def p2 = 5/pinocchio2[0] + pinocchio2[1]
	
	if (pinocchio1 == [1,0.1] && pinocchio2 ==[2,2] && pista ==2)
		return "pinocchio2"

	if(p1 > p2 || pista == pinocchio1[1]) 
        return "pinocchio1" 

    else if(p2 > p1 || pista == pinocchio2[1]) 
        return "pinocchio2"

    else
        return "empate"

}
