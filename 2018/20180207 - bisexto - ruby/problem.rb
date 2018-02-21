def bisexto(ano)
	if 
		(ano % 4 == 0 && ano % 100 == 0 && ano % 400 == 0) || 
		(ano % 4 == 0 && ano % 100 != 0)
		return true
	end	

	return false	    
	
end