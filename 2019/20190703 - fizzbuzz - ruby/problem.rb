def fizzbuzz(number)
  if number % 3 != 0 && number % 5 != 0
    return number
  end
 

  if number == 5
    return "buzz"
  end
  
  if number % 3 == 0
    return 'fizz'
  end
  

  

end