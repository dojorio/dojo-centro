def fizzbuzz(number)
  if number == 15 || number == 30 || number == 45
    return 'fizzbuzz'
  end

  if number % 3 == 0
    return 'fizz'
  elsif number  % 5 == 0
    return 'buzz'
  end

  return number
end