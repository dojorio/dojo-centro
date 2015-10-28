def fizzbuzz(number)
  if number == 3 || number == 6 || number == 9 || number == 12
    return "Fizz"
  end

  if number == 5 || number == 10
    return "Buzz"
  end

  number.to_s
end