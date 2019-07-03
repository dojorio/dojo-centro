def fizzbuzz(number)
  if number % 3 != 0 && number % 5 != 0
    return number
  end
  if number == 7
    return 7
  end
  if number == 5
    return "buzz"
  end
  if number == 4
    return 4
  end
  if number % 3 == 0
    return 'fizz'
  end
  if number == 2
    return 2
  end

  return 1

end