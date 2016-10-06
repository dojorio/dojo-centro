def urinal(pissers)
  vacancies = 0
  (1...(pissers.length)).each do |index| 
    if pissers[index-1] == '.' && pissers[index] == '.'
      vacancies += 1
    elsif pissers[index-1] != pissers[index]
      vacancies -= 1
    end
  end
  [vacancies, 0].max 
end