def urinal(pissers)
	vacancies = 0

	pissers.split('').each do |pisser|
		vacancies += 1 if pisser == '.'
	end 
	vacancies
end