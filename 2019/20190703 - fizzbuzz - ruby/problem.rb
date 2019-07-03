def fizzbuzz(number)
  if number % 15 == 0 
    return 'fizzbuzz'
  end

  if number % 5 == 0
    return "buzz"
  end

  if number % 3 == 0
    return 'fizz'
  end

  return number
  
end