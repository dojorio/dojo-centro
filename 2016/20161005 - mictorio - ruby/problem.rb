def urinal(pissers)
  if pissers.length > 1
    return 0 if !pissers.include?('..') 
  end

  vacancies = pissers.length.fdiv(2).ceil

  pissers.split('').each do |pisser|
    vacancies -= 1 if pisser == '*'
  end

  vacancies
end