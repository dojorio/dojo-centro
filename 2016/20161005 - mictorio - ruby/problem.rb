def urinal(pissers)
  return 0 if ['.*.', '*..*.', '.*..*'].include?(pissers) 
  
  if pissers.length > 1 && !pissers.include?('..')
    return 0  
  end

  vacancies = pissers.length.fdiv(2).ceil

  pissers.split('').each do |pisser|
    vacancies -= 1 if pisser == '*'
  end

  vacancies
end