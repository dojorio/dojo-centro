def fizzbuzz(number)  
  if number % 15 == 0
    return "FizzBuzz"
  end  

  if number % 5 == 0
    return "Buzz"
  end

  if number % 3 == 0
    return "Fizz"      
  end  

  number
end