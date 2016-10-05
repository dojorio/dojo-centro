def urinal(pissers)
  return 0 if ['.*.', '*..*.'].include?(pissers) 

  vacancies = pissers.length.fdiv(2).ceil

  pissers.split('').each do |pisser|
    vacancies -= 1 if pisser == '*'
  end

  vacancies
end