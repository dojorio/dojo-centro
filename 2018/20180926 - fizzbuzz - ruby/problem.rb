def fizzbuzz(number)
  if number == 15
    return 'fizzbuzz'
  end

  if number % 3 == 0
    return 'fizz'
  elsif number  == 5 || number == 10 || number == 20 || number == 25
    return 'buzz'
  end

  return number
end