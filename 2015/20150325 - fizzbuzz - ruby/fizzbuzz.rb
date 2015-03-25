def fizzbuzz(number)
  if number % 5 == 0
    return "Buzz"
  end
  if number % 3 == 0
    return "Fizz"      
  end  
  return number
end