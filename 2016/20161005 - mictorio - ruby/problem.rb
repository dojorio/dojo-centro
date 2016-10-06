def urinal(pissers)
  # return 0 if ['.*.', '*..*.', '.*..*', '.*..*.'].include?(pissers) 
  
  # if pissers.length > 1 && !pissers.include?('..')
  #   return 0
  # end

  # vacancies = pissers.length.fdiv(2).ceil

  # pissers.split('').each do |pisser|
  #   vacancies -= 1 if pisser == '*'
  # end

  # vacancies
  vacancies = 0
  (1...(pissers.length)).each do |index| 
    if pissers[index-1] == '.' && pissers[index] == '.'
      vacancies += 1
    elsif pissers[index] == '*'
      vacancies -= 1
    end
  end
  vacancies
end