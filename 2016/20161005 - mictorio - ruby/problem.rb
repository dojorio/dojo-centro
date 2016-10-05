def urinal(pissers)
	vacancies = 0

	pissers.each do |pisser|
		vacancies += 1 if pisser == '.'
	end 
end