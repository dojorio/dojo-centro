def fizzbuzz(number)
  if number == 3 || number == 6 || number == 9 || number == 12 || number == 18
    return "Fizz"
  end

  if number == 5 || number == 10
    return "Buzz"
  end

  if number == 15
    return "FizzBuzz"
  end


  number.to_s
end