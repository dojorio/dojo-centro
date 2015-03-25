def fizzbuzz(number)  
  resposta = ""
  if number % 3 == 0
    resposta = "Fizz"      
  end  

  if number % 5 == 0
    resposta += "Buzz"
  end

  resposta == ""? number : resposta
end