def fizzbuzz(number)

  return 'FizzBuzz' if number % 15 == 0
  
  return 'Fizz'     if number % 3  == 0

  return 'Buzz'     if number % 5  == 0

  number
end
