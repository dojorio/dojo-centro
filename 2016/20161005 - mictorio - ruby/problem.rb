def urinal(pissers)
	return 2 if pissers == '....'
	return 1 if pissers.include?('...') && pissers.length 
	return 1 if pissers.include?('..') && pissers.length < 4
  pissers == '.' ? 1 : 0 
end