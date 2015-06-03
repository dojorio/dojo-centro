def static calcula (amp1, amp2) {
	def amps = [amp1, amp2]

	if (1 in amps || 3 in amps)
            return 3

        else if ((amp1 - amp2).abs() == 1 ) 
	    
	    amp1 * amp2 / 10 * amps.min()
	
        else if (amps.max() == 8)
            amps.max()

        else if (amps.min() == 5)
            amps.min() * 2
	
        else
            amps.max()
}


