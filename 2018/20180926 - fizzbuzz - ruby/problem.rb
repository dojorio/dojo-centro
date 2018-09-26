def fizzbuzz(number)
  
  if number % 15 == 0
    return 'fizzbuzz'
  elsif number % 3 == 0
    return 'fizz'
  elsif number  % 5 == 0
    return 'buzz'
  end

  return number
end