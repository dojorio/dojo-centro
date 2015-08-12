def pitagoras(*lista)
  result = 'tripla'
  lista.sort!

  if lista[0] ** 2 + lista[1] ** 2 == lista[2] ** 2 && lista[0]%2==0
    result << ' pitagorica'
  
  elsif lista[0] ** 2 + lista[1] ** 2 == lista[2] ** 2 
    result << ' pitagorica primitiva'
  end


  result
end