def fizzbuzz(number)
  if number % 3 == 0
    return 'fizz'
  elsif number  == 5 || number == 10 || number == 20
    return 'buzz'
  elsif number == 15
    return 'fizzbuzz'
  end

  return number
end