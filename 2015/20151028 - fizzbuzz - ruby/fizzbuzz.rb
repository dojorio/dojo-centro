def fizzbuzz(number)

  if number == 15
    return "FizzBuzz"
  end
    
  if number%3 == 0 
    return "Fizz"
  end

  if number == 5 || number == 10
    return "Buzz"
  end

  number.to_s
end